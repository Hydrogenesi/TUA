#!/bin/bash
# Automated PR merge script for TUA repository
# Merges PRs #8, #9, #10 in sequence with conflict resolution
# Usage: ./merge-prs.sh [--dry-run] [--force]

set -e

DRY_RUN=false
FORCE=false
REPO="Hydrogenesi/TUA"
MAIN_BRANCH="main"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            echo "🔍 DRY RUN MODE: No changes will be committed"
            shift
            ;;
        --force)
            FORCE=true
            echo "⚠️  FORCE MODE: Will overwrite conflicts"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}TUA PR Merge Automation Script${NC}"
echo -e "${BLUE}========================================${NC}"

# Check if git is available
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git is not installed${NC}"
    exit 1
fi

# Function to run command (or log in dry-run mode)
run_cmd() {
    if [ "$DRY_RUN" = true ]; then
        echo -e "${YELLOW}[DRY-RUN]${NC} $@"
    else
        echo -e "${BLUE}▶${NC} $@"
        "$@"
    fi
}

# Function to merge a PR
merge_pr() {
    local pr_number=$1
    local branch=$2
    local title=$3
    
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════${NC}"
    echo -e "${GREEN}Merging PR #${pr_number}: ${title}${NC}"
    echo -e "${GREEN}═══════════════════════════════════════${NC}"
    
    # Fetch latest
    echo -e "${BLUE}📥 Fetching from remote...${NC}"
    run_cmd git fetch origin
    
    # Checkout branch
    echo -e "${BLUE}🔀 Checking out branch: ${branch}${NC}"
    run_cmd git checkout "$branch"
    
    # Attempt rebase
    echo -e "${BLUE}🔄 Rebasing onto ${MAIN_BRANCH}...${NC}"
    if run_cmd git rebase "origin/${MAIN_BRANCH}"; then
        echo -e "${GREEN}✅ Rebase successful${NC}"
    else
        echo -e "${RED}⚠️  Rebase conflict detected${NC}"
        
        if [ "$FORCE" = true ]; then
            echo -e "${YELLOW}🔨 Resolving conflicts (FORCE mode)...${NC}"
            # Accept theirs (main branch) for all conflicts
            run_cmd git diff --name-only --diff-filter=U | while read file; do
                echo -e "${YELLOW}  Accepting main version of: $file${NC}"
                run_cmd git checkout --ours "$file"
                run_cmd git add "$file"
            done
            run_cmd git rebase --continue
            echo -e "${GREEN}✅ Conflicts resolved (accepted main branch versions)${NC}"
        else
            echo -e "${RED}❌ Rebase conflict. Please resolve manually:${NC}"
            echo ""
            echo "1. View conflicts:"
            echo "   git diff"
            echo ""
            echo "2. Edit conflicted files in your editor"
            echo ""
            echo "3. Stage resolved files:"
            echo "   git add <file>"
            echo ""
            echo "4. Continue rebase:"
            echo "   git rebase --continue"
            echo ""
            echo "5. Re-run this script"
            exit 1
        fi
    fi
    
    # Push to remote
    echo -e "${BLUE}📤 Pushing to remote...${NC}"
    run_cmd git push -f origin "$branch"
    
    # Checkout main for next merge
    if [ "$DRY_RUN" = false ]; then
        echo -e "${BLUE}🔀 Checking out main...${NC}"
        run_cmd git checkout "$MAIN_BRANCH"
        run_cmd git pull origin "$MAIN_BRANCH"
    fi
    
    echo -e "${GREEN}✅ PR #${pr_number} ready to merge${NC}"
}

# Main merge sequence
echo ""
echo -e "${BLUE}📋 Merge Plan:${NC}"
echo "  1. PR #8: copilot/align-documentation-with-codebase"
echo "  2. PR #9: copilot/add-plate71-renderer-specification"
echo "  3. PR #10: copilot/revise-plate71-renderer-specification"
echo ""

# PR #8
merge_pr 8 "copilot/align-documentation-with-codebase" "docs: replace ceremonial fiction with accurate MATRIUN documentation"

# PR #9
merge_pr 9 "copilot/add-plate71-renderer-specification" "Add Plate71 renderer specification and integrate it into project docs"

# PR #10
merge_pr 10 "copilot/revise-plate71-renderer-specification" "docs: Rewrite Plate71 renderer spec — ring topology & fractal architecture (v2.0)"

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✅ All PRs rebased and ready to merge!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "1. Go to GitHub: https://github.com/Hydrogenesi/TUA/pulls"
echo "2. Open each PR (#8, #9, #10 in order)"
echo "3. Click 'Merge pull request' button"
echo "4. Confirm merge"
echo ""

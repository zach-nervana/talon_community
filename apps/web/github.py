import time
from talon.voice import Context, Key, press
from . import browser

BROWSERS = ["com.google.Chrome", "org.mozilla.firefox"]
ctx_global = Context("github-sitewide", func=lambda app, win: app.bundle in BROWSERS)
ctx_repo = Context("github-repo", func=lambda app, win: in_repo_list(win.title))
ctx_editor = Context(
    "github-code-editor", func=lambda app, win: win.title.startswith("Editing")
)
ctx_issues_pull_lists = Context(
    "github-issues-pull-requests_lists",
    func=lambda app, win: win.title.startswith("Issues")
    or win.title.startswith("Pull Requests"),
)
ctx_issues_pull = Context(
    "github-issues-pull-requests",
    func=lambda app, win: " Issue " in win.title or " Pull Request " in win.title,
)
ctx_pull_changes = Context(
    "github-pull-request-changes", func=lambda app, win: " Pull Request " in win.title
)
ctx_network_graph = Context(
    "github-network-graph", func=lambda app, win: win.title.startswith("Network Graph")
)

# USER-DEFINED VARIABLES

repos = {"talon_community", "atom-talon", "NervanaSystems/coach"}
lag = 0.2


def in_repo_list(win_title):
    for repo in repos:
        if repo in win_title:
            return True
    return False


# SITE-WIDE METHODS


@browser.send_to_page
def search(m):
    press("/")


@browser.send_to_page
def goto_notifications(m):
    press("g")
    time.sleep(lag)
    press("n")


# REPO METHODS


@browser.send_to_page
def repo_goto_code(m):
    press("g")
    time.sleep(lag)
    press("c")


@browser.send_to_page
def repo_goto_issues(m):
    press("g")
    time.sleep(lag)
    press("i")


@browser.send_to_page
def repo_goto_pull_requests(m):
    press("g")
    time.sleep(lag)
    press("p")


@browser.send_to_page
def repo_goto_projects(m):
    press("g")
    time.sleep(lag)
    press("b")


@browser.send_to_page
def repo_goto_wiki(m):
    press("g")
    time.sleep(lag)
    press("w")


@browser.send_to_page(stay_in_page_mode=True)
def repo_find_file(m):
    press("t")


@browser.send_to_page(stay_in_page_mode=True)
def repo_switch_branch(m):
    press("w")


# ISSUES AND PULL REQUESTS LISTS METHODS


@browser.send_to_page(stay_in_page_mode=True)
def create_issue(m):
    press("c")


@browser.send_to_page(stay_in_page_mode=True)
def filter_by_author(m):
    press("u")


@browser.send_to_page(stay_in_page_mode=True)
def filter_by_label(m):
    press("l")


@browser.send_to_page(stay_in_page_mode=True)
def filter_by_milestone(m):
    press("m")


@browser.send_to_page(stay_in_page_mode=True)
def filter_by_assignee(m):
    press("a")


@browser.send_to_page
def open_issue(m):
    press("o")


# ISSUES AND PULL REQUESTS METHODS


@browser.send_to_page(stay_in_page_mode=True)
def request_reviewer(m):
    press("q")


@browser.send_to_page(stay_in_page_mode=True)
def set_milestone(m):
    press("m")


@browser.send_to_page(stay_in_page_mode=True)
def apply_label(m):
    press("l")


@browser.send_to_page(stay_in_page_mode=True)
def set_assignee(m):
    press("a")


def close_issue_and_submit_comment(m):
    # NOTE: this only works if the cursor is in the comment you are submitting
    press("cmd-shift-enter")
    browser.tridactyl_mode()


# PULL REQUEST CHANGES METHODS


@browser.send_to_page
def list_commits(m):
    press("c")


@browser.send_to_page
def list_changed_files(m):
    press("t")


# NETWORK GRAPH METHODS


@browser.send_to_page
def scroll_left(m):
    press("h")


@browser.send_to_page
def scroll_right(m):
    press("l")


@browser.send_to_page
def scroll_down(m):
    press("j")


@browser.send_to_page
def scroll_up(m):
    press("k")


@browser.send_to_page
def scroll_left_most(m):
    press("shift-h")


@browser.send_to_page
def scroll_right_most(m):
    press("shift-l")


@browser.send_to_page
def scroll_down_most(m):
    press("shift-j")


@browser.send_to_page
def scroll_up_most(m):
    press("shift-k")


# TODO: create a site wide context
ctx_repo.keymap({})

ctx_repo.keymap(
    {
        "[go to] code": repo_goto_code,
        "[go to] issues": repo_goto_issues,
        "[go to] (pull | pulls)[requests]": repo_goto_pull_requests,
        "[go to] projects": repo_goto_projects,
        "[go to] wiki": repo_goto_wiki,
        "(find file | peach)": repo_find_file,
        "switch [(branch | tag)]": repo_switch_branch,
        # TODO: create a site wide context
        "jet search": search,
        "notifications": goto_notifications,
        # '(hover)': hover,
    }
)

ctx_editor.keymap(
    {
        "(search | find)": Key("cmd-f"),
        "[find] next": Key("cmd-g"),
        "[find] prev": Key("shift-cmd-g"),
        "replace": Key("cmd-alt-f"),
        "replace all": Key("shift-cmd-alt-f"),
        "(go to | jump to) [line]": Key("alt-g"),
        "undo": Key("cmd-z"),
        "redo": Key("cmd-y"),
    }
)

ctx_issues_pull_lists.keymap(
    {
        "(create | new) [issue] [pull request]": create_issue,
        "[filter] [by] author": filter_by_author,
        "[filter] [by] label": filter_by_label,
        "[filter] [by] milestone": filter_by_milestone,
        "[filter] [by] [(worker | assigned | assignee)]": filter_by_assignee,
        "open [issue] [pull request]": open_issue,
    }
)

ctx_issues_pull.keymap(
    {
        "(request | assign) (reviewer | review)": request_reviewer,
        "[set] milestone": set_milestone,
        "[apply] label": apply_label,
        "assign": set_assignee,
        "close and comment": close_issue_and_submit_comment,
    }
)

ctx_pull_changes.keymap(
    {
        "[list] commits": list_commits,
        "[list] [changed] files": list_changed_files,
        "down": Key("j"),
        "up": Key("k"),
        "[add] [diff] comment": Key("cmd-shift-enter"),
    }
)

ctx_network_graph.keymap(
    {
        "[scroll] left": scroll_left,
        "[scroll] right": scroll_right,
        "[scroll] down": scroll_down,
        "[scroll] up": scroll_up,
        "[scroll] left most": scroll_left_most,
        "[scroll] right most": scroll_right_most,
        "[scroll] down most": scroll_down_most,
        "[scroll] up most": scroll_up_most,
    }
)

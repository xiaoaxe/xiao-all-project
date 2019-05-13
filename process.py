#!/usr/bin/env python
# encoding: utf-8

#
"""
@description: 处理github返回的数据，用于生成md的文件列表

@author: pacman
@time: 2017/10/9 21:03
"""

import requests
import json
import re

url = 'https://api.github.com/users/githubao/repos?per_page=100'

prefix_fmt = 'https://github.com/{}'

url_pat = re.compile('\((https://github.com/githubao/.*?)\)')


def get_password():
    with open('/Users/baoqiang/Downloads/ps.txt', 'r', encoding='utf-8') as f:
        user, password = f.read().strip().split(' ')
        return user, password


def run2():
    # local
    local_set = set()

    with open('README.md', 'r', encoding='utf-8') as f:
        for line in f:
            m = url_pat.search(line)
            if m:
                local_set.add(m.group(1))

    # server
    server_set = set()

    response = requests.get(url, auth=get_password())
    repos = json.loads(response.content.decode())
    for repo in repos:
        repo_name = prefix_fmt.format(repo['full_name'])
        server_set.add(repo_name)

    print('server repos len: {}'.format(len(repos)))
    print('local repos len: {}'.format(len(local_set)))

    diff_set = (item for item in server_set if item not in local_set)
    print('\n'.join(diff_set))


def run():
    with open('README.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = ''.join(lines)

    response = requests.get(url)
    repos = json.loads(response.content.decode())
    for repo in repos:
        repo_name = prefix_fmt.format(repo['full_name'])

        if repo_name not in data:
            print(repo_name)

    print('remote repo len: {}'.format(len(repos)))
    print('local file len: {}'.format(len([item for item in lines if item.startswith('-')])))


def main():
    run2()


if __name__ == '__main__':
    main()

"""

{
"id": 89593071,
"name": "beauty-of-programming",
"full_name": "githubao/beauty-of-programming",
"owner": {},
"private": false,
"html_url": "https://github.com/githubao/beauty-of-programming",
"description": "<beauty of programming> src code",
"fork": false,
"url": "https://api.github.com/repos/githubao/beauty-of-programming",
"forks_url": "https://api.github.com/repos/githubao/beauty-of-programming/forks",
"keys_url": "https://api.github.com/repos/githubao/beauty-of-programming/keys{/key_id}",
"collaborators_url": "https://api.github.com/repos/githubao/beauty-of-programming/collaborators{/collaborator}",
"teams_url": "https://api.github.com/repos/githubao/beauty-of-programming/teams",
"hooks_url": "https://api.github.com/repos/githubao/beauty-of-programming/hooks",
"issue_events_url": "https://api.github.com/repos/githubao/beauty-of-programming/issues/events{/number}",
"events_url": "https://api.github.com/repos/githubao/beauty-of-programming/events",
"assignees_url": "https://api.github.com/repos/githubao/beauty-of-programming/assignees{/user}",
"branches_url": "https://api.github.com/repos/githubao/beauty-of-programming/branches{/branch}",
"tags_url": "https://api.github.com/repos/githubao/beauty-of-programming/tags",
"blobs_url": "https://api.github.com/repos/githubao/beauty-of-programming/git/blobs{/sha}",
"git_tags_url": "https://api.github.com/repos/githubao/beauty-of-programming/git/tags{/sha}",
"git_refs_url": "https://api.github.com/repos/githubao/beauty-of-programming/git/refs{/sha}",
"trees_url": "https://api.github.com/repos/githubao/beauty-of-programming/git/trees{/sha}",
"statuses_url": "https://api.github.com/repos/githubao/beauty-of-programming/statuses/{sha}",
"languages_url": "https://api.github.com/repos/githubao/beauty-of-programming/languages",
"stargazers_url": "https://api.github.com/repos/githubao/beauty-of-programming/stargazers",
"contributors_url": "https://api.github.com/repos/githubao/beauty-of-programming/contributors",
"subscribers_url": "https://api.github.com/repos/githubao/beauty-of-programming/subscribers",
"subscription_url": "https://api.github.com/repos/githubao/beauty-of-programming/subscription",
"commits_url": "https://api.github.com/repos/githubao/beauty-of-programming/commits{/sha}",
"git_commits_url": "https://api.github.com/repos/githubao/beauty-of-programming/git/commits{/sha}",
"comments_url": "https://api.github.com/repos/githubao/beauty-of-programming/comments{/number}",
"issue_comment_url": "https://api.github.com/repos/githubao/beauty-of-programming/issues/comments{/number}",
"contents_url": "https://api.github.com/repos/githubao/beauty-of-programming/contents/{+path}",
"compare_url": "https://api.github.com/repos/githubao/beauty-of-programming/compare/{base}...{head}",
"merges_url": "https://api.github.com/repos/githubao/beauty-of-programming/merges",
"archive_url": "https://api.github.com/repos/githubao/beauty-of-programming/{archive_format}{/ref}",
"downloads_url": "https://api.github.com/repos/githubao/beauty-of-programming/downloads",
"issues_url": "https://api.github.com/repos/githubao/beauty-of-programming/issues{/number}",
"pulls_url": "https://api.github.com/repos/githubao/beauty-of-programming/pulls{/number}",
"milestones_url": "https://api.github.com/repos/githubao/beauty-of-programming/milestones{/number}",
"notifications_url": "https://api.github.com/repos/githubao/beauty-of-programming/notifications{?since,all,participating}",
"labels_url": "https://api.github.com/repos/githubao/beauty-of-programming/labels{/name}",
"releases_url": "https://api.github.com/repos/githubao/beauty-of-programming/releases{/id}",
"deployments_url": "https://api.github.com/repos/githubao/beauty-of-programming/deployments",
"created_at": "2017-04-27T12:05:27Z",
"updated_at": "2017-04-27T14:57:14Z",
"pushed_at": "2017-04-27T14:57:13Z",
"git_url": "git://github.com/githubao/beauty-of-programming.git",
"ssh_url": "git@github.com:githubao/beauty-of-programming.git",
"clone_url": "https://github.com/githubao/beauty-of-programming.git",
"svn_url": "https://github.com/githubao/beauty-of-programming",
"homepage": null,
"size": 4,
"stargazers_count": 0,
"watchers_count": 0,
"language": "C++",
"has_issues": true,
"has_projects": true,
"has_downloads": true,
"has_wiki": true,
"has_pages": false,
"forks_count": 0,
"mirror_url": null,
"open_issues_count": 0,
"forks": 0,
"open_issues": 0,
"watchers": 0,
"default_branch": "master"
}

"""

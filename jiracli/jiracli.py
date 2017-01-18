#!/usr/bin/env python
import os
import click
import logging
import json
import ConfigParser
import requests
from datetime import datetime
from jira import JIRA

@click.group()
def cli():

        #jira = JIRA('https://spscommerce.atlassian.net',basic_auth=(user,password))
        jira = '10'

@cli.command()
@click.pass_context
# default to sev1 + summary
# --all
# --mine
def active():
    """ Shows incidents that are currently active."""
    click.echo(jira)
    #pass


@cli.command()
def comment(incident):
    """ Add a comment to an incident."""
    pass


@cli.command()
def grab(incident):
    """ Assigns and incident to you."""
    pass


@cli.command()
def status(incident):
    """ Change the status of an incident."""
    pass


@cli.command()
# mine
# details
def show(incident):
    """ Change the status of an incident."""
    pass


def create_command(holder, filter):
    """ If custom filters are defined in ~/.jiracli they are translated into
    command arguments.
    """
    @cli.command(holder)
    def holder_test():
        print holder
    return holder

def run_search(account, query):
    url = "https://{}.atlassian.net/rest/api/2/search".format(account)
    payload = {
    "jql": query
    }

# @cli.command()
# @create_command
# def a_func():
#     print 'stuff'
#
#     # Create a JIRA connection
#     jira = JIRA('https://spscommerce.atlassian.net',basic_auth=(JIRA_USER, JIRA_PASS))
#
#     input_jql = event['jira']['jql']
#     jira_key = event['jira']['jira_key']
#     logger.debug("Checking the following jql: {0}".format(input_jql))
#
#     jql_results = jira.search_issues(input_jql)
#
#     msg = "Recent CHGMGMT JIRA Issues:\n"
#     for i in jql_results:
#         logger.debug("Found issue in given jql: {0}".format(i))
#         summary = i.fields.summary
#         msg += "{0} - {1}\n".format(i, summary)
#
#     if jira_key:
#         jira_commenter(msg, jira_key)
#
if __name__ == '__main__':
    jira_conf = os.environ['HOME']+ '/.jiracli'
    config = ConfigParser.ConfigParser()
    config.read(jira_conf)

    if 'creds' in config.sections():
        user = config.get('creds', 'user')
        password = config.get('creds', 'pass')
        account = config.get('creds', 'account')
    elif os.getenv('JIRA_USER'):
        user = os.environ['JIRA_USER']
        password = os.environ['JIRA_PASS']
        account = os.environ['JIRA_ACCOUNT']
    else:
        user = click.prompt('Enter username: ')
        password = click.prompt('Enter password: ')
        account = click.promt('Enter account name: ')

    if 'filters' in config.sections():
        for k,v in config.items('filters'):
            create_command(k, v)
        #custom_filters(config.items('filters'))
    else:
        print 'no custom commands found'
    cli()

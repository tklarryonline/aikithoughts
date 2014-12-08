import sure

from behave import given, when, then
from tests.features.steps.utils import visit_url


@given(u'the website is on')
def given_the_website_is_on(context):
    context.browser.get('https://aikithoughts-stag.herokuapp.com')

@when(u'I visit "{endpoint}"')
def step_impl(context, endpoint):
    visit_url(context.browser, endpoint)

@then(u'I should see "{text}" in the page title')
def step_impl(context, text):
    context.browser.title.should.contain(text)

@then(u'I should see text "{text}"')
def step_impl(context, text):
    context.browser.page_source.should.contain(text)
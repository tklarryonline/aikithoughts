from behave import given, when, then
from tests.features.steps.utils import visit_url


@when(u'I visit the homepage')
def step_impl(context):
    visit_url(context.browser)
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
def dash_value(i,count):
	value = count[i]
	return value


@register.filter()
def capacity_check(count,val):
	if val > count:
		status = 'normal'
	elif val < count:
		status = 'capacity'
	else:
		status = 'normal'
	return status


@register.filter(name='convert_time')
def convert_time(value):
	val = format(value,'%H:%M')
	return val

@register.simple_tag
def define(value=None):
	return value
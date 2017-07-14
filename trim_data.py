# -*- coding: utf-8 -*-
"""
Created on 7/14/17
Author: Jihoon Kim
"""

import feature_index


def drop_null_columns(data):
    """Drop columns (most of values are null)"""
    data.drop(feature_index.null_cols, axis=1, inplace=True)
    return None


def drop_emp_title(data):
    data.drop('emp_title', axis=1, inplace=True)
    return None


def drop_url(data):
    data.drop('url', axis=1, inplace=True)
    return None


def drop_zip_code(data):
    data.drop('zip_code', axis=1, inplace=True)
    return None

def drop_earliest_cr_line(data):
    data.drop('earliest_cr_line', axis=1, inplace=True)
    return None

def drop_out_prncp(data):
    data.drop('out_prncp', axis=1, inplace=True)
    return None

def drop_out_prncp_inv(data):
    data.drop('out_prncp_inv', axis=1, inplace=True)
    return None

def drop_total_rec_late_fee(data):
    data.drop('total_rec_late_fee', axis=1, inplace=True)
    return None

def drop_recoveries(data):
    data.drop('recoveries', axis=1, inplace=True)
    return None

def split_loan_in_progress(data):
    """Return table of loan in progress. It drops the loan in progress from loan data internally."""
    progress_bool = data.loan_status.isin(feature_index.in_progress_index)
    loan_in_progress = data[progress_bool].drop('loan_status', axis=1)
    data.drop(list(loan_in_progress.index), axis=0, inplace=True)
    return loan_in_progress


def categorize_target(data):
    """Returns encoded loan status: Safe, Warning and Bad"""

    def func(x):
        if x['loan_status'] in feature_index.bad_index:
            return 0
        elif x['loan_status'] in feature_index.warning_index:
            return 1
        else:
            return 2

    data['loan_status_coded'] = data.apply(func, axis=1)
    data.drop('loan_status', axis=1, inplace=True)
    return data


def ext_num_from_sub_grade(data):
    data['sub_grade'] = data['sub_grade'].map(lambda x: int(x.lstrip('ABCDEFG')))
    return data


def fill_na_annual_inc(data):
    data.annual_inc.fillna(data.annual_inc.median(), inplace=True)
    return None


def fill_na_title(data):
    data.title.fillna('Unknown', inplace=True)
    return None

def fill_na_delinq_2yrs(data):
    data.delinq_2yrs.fillna(data.delinq_2yrs.median(), inplace=True)
    return None

def fill_na_inq_last_6mths(data):
    data.inq_last_6mths.fillna(data.inq_last_6mths.median(), inplace=True)
    return None

def fill_na_open_acc(data):
    data.open_acc.fillna(data.open_acc.median(), inplace=True)
    return None

def fill_na_pub_rec(data):
    data.pub_rec.fillna(data.pub_rec.median(), inplace=True)
    return None

def fill_na_revol_util(data):
    data.revol_util.fillna(data.revol_util.median(), inplace=True)
    return None

def fill_na_total_acc(data):
    data.total_acc.fillna(data.total_acc.median(), inplace=True)
    return None

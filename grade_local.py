#!/usr/bin/env python3

"""
Do a local practice grading.
The score you recieve here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.
"""

import os
import sys

import numpy

import cse40.assignment
import cse40.question
import cse40.style
import cse40.utils

def true_hypothesis(feature, theta):
    return True

class T1A(cse40.question.Question):
    def score_question(self, submission):
        result = submission.threshold_hypothesis(0, 0)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, bool)):
            self.fail("Function must return a boolean value.")
            return

        self.full_credit()

class T1B(cse40.question.Question):
    def score_question(self, submission):
        result = submission.zero_one_loss(0, True, true_hypothesis, 0)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")
            return

        self.full_credit()

class T2A(cse40.question.Question):
    def score_question(self, submission):
        result = submission.expected_loss([0] * 4, [True] * 4, submission.zero_one_loss,
                true_hypothesis, 0)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")
            return

        self.full_credit()

class T2B(cse40.question.Question):
    def score_question(self, submission):
        result = submission.index_of_minimum([1, 2, 3])
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")
            return

        self.full_credit()

class T3A(cse40.question.Question):
    def score_question(self, submission):
        function_names = [
            'true_positive_fraction',
            'false_positive_fraction',
            'true_negative_fraction',
            'false_negative_fraction',
        ]

        for name in function_names:
            function = getattr(submission, name)
            result = function([0], [True], true_hypothesis, 0)

            if (isinstance(result, type(NotImplemented))):
                self.add_message("%s() not implemented." % (name))
                continue

            if (not isinstance(result, (float, numpy.float64, numpy.float32))):
                self.fail("%s() must return a float.")
                continue

            self.score += 1

class T3B(cse40.question.Question):
    def score_question(self, submission):
        function_names = [
            'true_positive_rate',
            'false_positive_rate',
            'true_negative_rate',
            'false_negative_rate',
        ]

        for name in function_names:
            function = getattr(submission, name)
            result = function([0], [True], true_hypothesis, 0)

            if (isinstance(result, type(NotImplemented))):
                self.add_message("%s() not implemented." % (name))
                continue

            if (not isinstance(result, (float, numpy.float64, numpy.float32))):
                self.fail("%s() must return a float.")
                continue

            self.score += 1

def grade(path):
    submission = cse40.utils.prepare_submission(path)

    questions = [
        T1A("Task 1.A (threshold_hypothesis)", 1),
        T1B("Task 1.B (zero_one_loss)", 1),
        T2A("Task 2.A (expected_loss)", 1),
        T2B("Task 2.B (index_of_minimum)", 1),
        T3A("Task 3.A (fractions)", 4),
        T3B("Task 3.B (rates)", 4),
        cse40.style.Style(path, max_points = 1),
    ]

    assignment = cse40.assignment.Assignment("Practice Grading for Hands-On 2", questions)
    assignment.grade(submission)

    return assignment

def main(path):
    assignment = grade(path)
    print(assignment.report())

def _load_args(args):
    exe = args.pop(0)
    if (len(args) != 1 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s <submission path (.py or .ipynb)>" % (exe), file = sys.stderr)
        sys.exit(1)

    path = os.path.abspath(args.pop(0))

    return path

if (__name__ == '__main__'):
    main(_load_args(list(sys.argv)))

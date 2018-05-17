# This Python file uses the following encoding: utf-8


from helper import verify_conversion


def test_colon():
    verify_conversion(
        '''
This is a colon test : explanation
        ''',
        '''
This is a colon test~: explanation
        ''',
        'latex'
    )


def test_ponctuations():
    verify_conversion(
        '''
This is a semi-colon test ; explanation

This is a exclamation mark test !

This is a question mark test ?
        ''',
        '''
This is a semi-colon test\\thinspace{}; explanation

This is a exclamation mark test\\thinspace{}!

This is a question mark test\\thinspace{}?
        ''',
        'latex'
    )


def test_space_quotes():
    verify_conversion(
        '''
« This is a quoted test »

‹ This is a quoted test ›

“ This is a quoted test ”
        ''',
        '''
«\\thinspace{}This is a quoted test\\thinspace{}»

‹\\thinspace{}This is a quoted test\\thinspace{}›

"\\thinspace{}This is a quoted test\\thinspace{}"
        ''',
        'latex'
    )

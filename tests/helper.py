# This Python file uses the following encoding: utf-8

from panflute import convert_text

import pandoc_latex_french_spaces


def verify_conversion(markdown, expected, format='markdown'):
    doc = convert_text(markdown, standalone=True)
    doc.format = format
    pandoc_latex_french_spaces.main(doc)
    converted = convert_text(
        doc.content,
        input_format='panflute',
        output_format='markdown',
        extra_args=['--wrap=none'],
        standalone=True
    )
    assert converted == expected.strip()

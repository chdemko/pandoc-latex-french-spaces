from unittest import TestCase
from panflute import convert_text

import pandoc_latex_french_spaces


class FrenchSpacesTest(TestCase):
    def verify_conversion(self, markdown, expected, format="markdown"):
        doc = convert_text(markdown, standalone=True)
        doc.format = format
        pandoc_latex_french_spaces.main(doc)
        converted = convert_text(
            doc.content,
            input_format="panflute",
            output_format="markdown",
            extra_args=["--wrap=none"],
            standalone=True,
        )
        self.assertEqual(converted, expected.strip())

    def test_colon(self):
        self.verify_conversion(
            """
This is a colon test : explanation
            """,
            """
This is a colon test`~`{=tex}: explanation
            """,
            "latex",
        )

    def test_ponctuations(self):
        self.verify_conversion(
            """
This is a semi-colon test ; explanation

This is a exclamation mark test !

This is a question mark test ?
            """,
            """
This is a semi-colon test`\\thinspace{}`{=tex}; explanation

This is a exclamation mark test`\\thinspace{}`{=tex}!

This is a question mark test`\\thinspace{}`{=tex}?
            """,
            "latex",
        )

    def test_space_quotes(self):
        self.verify_conversion(
            """
« This is a quoted test »

‹ This is a quoted test ›

“ This is a quoted test ”
            """,
            """
«`\\thinspace{}`{=tex}This is a quoted test`\\thinspace{}`{=tex}»

‹`\\thinspace{}`{=tex}This is a quoted test`\\thinspace{}`{=tex}›

"`\\thinspace{}`{=tex}This is a quoted test`\\thinspace{}`{=tex}"
            """,
            "latex",
        )

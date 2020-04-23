from titlecase import titlecase


class TitleCaseTests:
    def test_lower_text_is_uppercased_correctly(self):
        initial_text = 'this should be capitalized'
        expected_text = 'This Should Be Capitalized'
        result_text = titlecase.title_case(initial_text)
        assert result_text == expected_text


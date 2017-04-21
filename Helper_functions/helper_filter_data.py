"""Use this in your main script for fl_interactive_users to filter data from different columns."""

    def _helper_filter_data(self, row):
        columns = ['PhoneBusiness', 'PhoneMobile', 'PhonePager', 'PhoneHome', 'PhoneAssistant', 'FaxBusiness', 'FaxHome', 'EmailPersonal', 'EmailAddress', 'EmailAssistant']
        a_dict = {'email': [], 'phone': []}
        final_dict = {}

        for column in columns:
            value = self._prep_text_field(row, column)
            if value and value != '':
                if '@' in value:
                    a_dict['email'].append('%s:%s' % (column, value))

                elif len([x for x in value if x.isdigit()]) >= 8:
                    a_dict['phone'].append('%s:%s' % (column, value))

        final_dict['email'] = ';'.join(a_dict['email'])
        final_dict['phone'] = ';'.join(a_dict['phone'])

        return final_dict


    def _directoryTelephone(self, row):
        value = self._helper_filter_data(row)['phone']
        if value and value != '':
            return value.split(';', 1)[0].split(':')[1]

    def _directoryTelephoneLabel(self, row):
        value = self._helper_filter_data(row)['phone']
        if value and value != '':
            return value.split(';', 1)[0].split(':')[0]

    def _directoryAdditionalTelephones(self, row):
        value = self._helper_filter_data(row)['phone']
        if value and value != '' and len(value.split(';', 1)) == 2:
            return self._create_label_value_structure(value.split(';', 1)[1])
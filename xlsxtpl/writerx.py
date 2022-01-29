# -*- coding: utf-8 -*-

from xltpl.writerx import BookWriter as BookWriterBase


class BookWriter(BookWriterBase):


    def render_sheet(self, payload, *args, **kwargs):
        if len(args)>0:
            payload['sheet_name'] = args[0]

        if len(args)>1:
            payload['tpl_index'] = args[1]

        return BookWriterBase.render_sheet(self, payload)

    def get_tpl_idx(self, payload):
        idx = payload.get('tpl_idx')
        if not idx:
            idx = 0
        return idx

    def get_sheet_name(self, payload, key=None):
        name = payload.get('sheet_name')
        if not name:
            if key:
                name = key
            else:
                name = 'XLSheet%d' % len(self.workbook._sheets)
        return name

    def render_book2(self, payloads):
        for payload in payloads:
            idx = self.get_tpl_idx(payload)
            sheet_name = self.get_sheet_name(payload)
            self.render_sheet(payload['ctx'], sheet_name, idx)


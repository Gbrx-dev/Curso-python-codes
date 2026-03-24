from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('qualquer coisa')
lp.log_success('sucesso')
lf = LogPrintMixin()
lf.log_error('qualquer coisa')
lp.log_success('sucesso')

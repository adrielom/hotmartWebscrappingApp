def quotes_filtering(args):
    single_quote_filter = args.replace("'", r"""\'""")
    double_quote_filter = single_quote_filter.replace('"', r"""\"""")
    return double_quote_filter

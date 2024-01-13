from django.utils.safestring import mark_safe


def show_data_colored_block(
    color="Green",
    text="",
    text_bold=False,
    link_href=None,
):

    link_text = (
        f"""<a href="{link_href}" style="color:white;
        font-size:14px;padding:0px;">"""
        if link_href
        else ""
    )

    return mark_safe(
        f"""<div style="display: inline-flex; padding:5px 10px 5px 10px;font-size:16px;
        {'font-weight: 700;' if text_bold else ''}
        margin-bottom:5px;margin-right:5px;line-height: 1;text-align: center;
        vertical-align:baseline;border-radius:5px;
        color: #fff;background-color: {color}">
        {link_text}{text}{'</a>' if link_text else ''}
        </div>
        """
    )


def show_data_colored_badge(color="Green", text_bold=False, text="", extra_styles=""):

    return mark_safe(
        f"""<div style="background-color: {color};display: inherit;
        padding:3px 8px 3px 8px;font-size: 14px;margin-bottom:5px;
        margin-bottom:5px;margin-right:5px;max-height: 30px; max-width: 150px;
        {'font-weight: 700;' if text_bold else ''}
        line-height: 1;text-align: center;min-width:50px;
        vertical-align: baseline;border-radius: 5px;{extra_styles}">{text}</div>"""
    )


def show_data_colored_border_block(
    color="Green",
    text="",
    text_bold=False,
    link_href=None,
    extra_styles="",
):

    link_text = (
        f"""<a href="{link_href}" style="color:white;
    font-size:14px;padding:0px;">"""
        if link_href
        else ""
    )

    return mark_safe(
        f"""<div style="background-color: #353535;display: inline-block;
        padding:5px 10px 5px 10px;{extra_styles}
        margin-bottom:5px;margin-right:5px;
        {'font-weight: 700;' if text_bold else ''}
        line-height: 1;text-align: left;min-width:50px;border-left:5px solid {color};
        min-width: 250px; max-width: 400px;
        vertical-align: baseline;border-radius:5px;font-size: 16px;">
        {link_text}{text}{'</a>' if link_text else ''}</div>"""
    )

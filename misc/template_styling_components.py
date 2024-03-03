from django.utils.safestring import mark_safe

from apps.test_progress.forms import CURRENT_STATUS_CODES


def show_test_card(
    test,
    test_progress,
):

    vertical_ticks = []
    for tick in range(1, test.test_max_result - 1)[::2]:
        vertical_ticks.append(
            f"""<div class="tick" 
            style="
            height: 50%;
            left: {100* (tick+1) / test.test_max_result}%; 
            top: -{(6 + tick)*25}%;
            " ></div>"""
        )

        if test_progress.result >= test.test_required_result:
            bar_background_color = "#96c83c"
        elif int(test_progress.current_status) == 2:
            bar_background_color = "#f04040"
        else:
            bar_background_color = "#808080"

        if test_progress.current_status in (0, 1):
            link_to_test = f"""
            <a href="/tests/{test_progress.pk}" 
                class="next_action_btn"  style="color:white;margin-top: 15px;">Пройти</a>
            """
        elif test_progress.current_status in (2, 3):
            link_to_test = f"""
            <a href="/tests/{test_progress.pk}" class="secondary_action_btn" style="margin-top: 15px;color:white;">
            <div  style="">
            Просмотреть</div></a>
            """
        else:
            link_to_test = ""

    result_bar_mergin_right = 2 if test_progress.result < test.test_max_result else 4

    if test_progress.current_status != 0:
        test_started = f"""
            <div class="test_result_passed_comment">
                <div class="test_notes_text test_result_passed_text">Начало прохождения</div>
                <div class="test_notes_text test_result_passed_points">{test_progress.attemp_started.strftime("%H:%M %d.%m.%Y")}</div>
            </div>
            """
    else:
        test_started = ""

    if test_progress.current_status in (2, 3):
        test_finished = f"""<div class="test_result_passed_comment">
                <div class="test_notes_text test_result_passed_text">Конец прохождения</div>
                <div class="test_notes_text test_result_passed_points">{test_progress.attemp_finished.strftime("%H:%M %d.%m.%Y")}</div>
            </div>"""

    else:
        test_finished = ""

    result = f"""
        <div class="test_card">
            <div class="test_header">
                <div class="test_header_title">{test.test_object_name}</div>
                <div class="test_header_status">
                    {dict(CURRENT_STATUS_CODES).get(str(test_progress.current_status))}
                </div>
            </div>
            
            <div>
                <div class="test_notes_text">Необходимо набрать: {test.test_required_result}</div>
                <div class="test_result_progress_bar">
                    <div class="test_result_progress_bar_bracket">
                        <div class="test_result_progress_bar_achieved_progress" style="
                        width: calc({min(100, 100* max(test_progress.result, 1) / test.test_max_result)}% - {result_bar_mergin_right}px);
                        background-color:{bar_background_color};"></div>
                        <div 
                            style="left: {100* test.test_required_result / test.test_max_result}%;" 
                            class="test_result_progress_bar_required_point">
                        </div>
                        {"".join(vertical_ticks)}
                    </div>
                    <div style="font-size: 15px;margin: auto;">
                        {str(max(test_progress.result, 0)) + ' / ' + str(test.test_max_result)}
                    </div>
                </div>
            </div>
            {test_started}
            {test_finished}
            {link_to_test}
            
        </div>
        """

    return mark_safe(result)

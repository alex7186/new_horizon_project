from django.utils.safestring import mark_safe

from apps.account_page.forms import CURRENT_STATUS_CODES


def show_test_result_card(
    test,
    test_progress,
):

    result = f"""
        <div style="border: 2px solid #e1e1e1; border-radius: 10px; 
        padding: 10px; margin-bottom: 20px;">
            <div style="display: flex;margin-bottom: 20px;">
                <div style="width:350px">{test.test_object_name}</div>
                <div style="font-size: 12px;color:#6e7a84;margin-left:auto;">
                    {dict(CURRENT_STATUS_CODES).get(str(test_progress.current_status))}
                </div>
            </div>
            
            <div>
                <div style="font-size:12px;margin-left:3px;color:grey;">Необходимо набрать: {test.test_required_result}</div>
                <div style="display: flex;">
                    <div style="border:1px solid grey;border-radius:5px;width:calc(100% - 80px);">
                        <div style="
                        width:{min(100, 100* test_progress.result / test.test_max_result)}%;
                        background-color:{'#96c83c' if test_progress.result >= test.test_required_result else '#f04040'};
                        height:100%; border-radius: 3px; 
                        "></div>
                        <div style="height: 100%; background-color: black; width: 2px;
                        position: relative;top: -100%; left: {100* test.test_required_result / test.test_max_result}%;"></div>
                    </div>
                    <div style="font-size: 15px;margin: auto;">
                        {str(test_progress.result) + ' / ' + str(test.test_max_result)}
                    </div>
                </div>
            </div>
        </div>
        """

    # {test.test_type}

    return mark_safe(result)


# <div class="tests_array">
#     <div class="show_test_passing">
#     <div class="test_card_name">

#         <div class="test_name">{{ test.header_text }}</div>
#     </div>
#     <div class="test_description">{{ test.detailed_text }}</div>

#     <div class="test_status">{{ test.current_status }}</div>
#     <div class="test_result">
#         {% if test.type == "bar" %}
#             {% if test.result > 50 %}
#                 <div class="test_result_green"><p>Пройдено</p></div>
#             {% else %}
#                 <div class="test_result_red"><p>Не пройдено</p></div>
#             {% endif %}

#         {% elif test.type == 1 %}
#             <div class="test_progress_frame">

#                 {% if test.result > 50 %}
#                 <div class="test_progress_bar test_progress_bar_green"
#                     style="width:{{ test.result }}%">
#                 {% else %}
#                 <div class="test_progress_bar test_progress_bar_red"
#                     style="width:{{ test.result }}%">
#                 {% endif %}
#                 </div>
#             </div>
#         {% endif %}
#     </div>
#     </div>
# </div>

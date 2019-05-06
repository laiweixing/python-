#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
import Common
import webbrowser
import time

# 报告生成时间
now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 生成本地html报告文件
def CreateReportHtml(data, testCaseFile):
    # 提取excel文件名中的数字
    testCaseFilenum = re.findall("\\d", testCaseFile)
    testCaseFilenum = testCaseFilenum[0]+testCaseFilenum[1]+testCaseFilenum[2]
    # 定义生成的html
    GEN_HTML = Common.gReportName+"testCase" + str(testCaseFilenum) + ".html"
    f = open(GEN_HTML, 'wb+')

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>测试报告</title>
        <style>
            *{margin: 0;padding: 0;}
            html,body{width: 100%;height: 100%;background-color: #FFFFF0;}
            /*头部关键信息栏*/
            article{width: 1080px;min-height: 2000%;margin: 0 auto;background-color: white;border: 1px double black;}
            .heading{width: 1080px;height:40px;margin: 0 10px;background-color: ;}
            #heading_r{width:1080px;}
            #recipients{background-color: #CDCDC1;border-radius: 8px;padding-left: 10px;padding-right: 10px;}
            #data_send{color:red;}
            .heading_{width: 1080px;height: 100px;margin: 10px 10px 0 10px;}
            .heading_t{width: 1060px;height: 50px;line-height: 50px;background-color: #7B68EE;}
            .heading_t h2{margin-left: 650px;}
            .heading_b{width: 1060px;height: 20px;margin-top: 20px;background-color: #7B68EE;}
            /*具体测试数据值*/
            #gk,#example{margin-top: 20px;font-size: 18px;}
            .gk{width: 1050px;height: 100px;margin: 10px 15px 0 15px;background-color: #C1FFC1;text-align: center;}
            .gk_one,.gk_two,.gk_three{width: 350px;height: 65px;line-height: 65px;float: left;}
            .gk_one_,.gk_two_,.gk_three_{width: 350px;height: 35px;line-height: 35px;float: left;}
            .example{width: 1050px;margin: 10px 15px 0 15px;}
            .example_sub{width: 128px;height: 65px;line-height: 65px;float: left;text-align: center;border:1px solid green;background-color: #87CEFA;}
            .example_Con{width: 128px;height: 130px;padding-top: 10px;float: left;border:1px solid green;background-color: #7FFFAA;}
            .example_Con2{width: 128px;height: 130px;float: left;border:1px solid green;background-color: red;}
            .example_con{width: 110px;height:120px;margin: 0 auto;font-size: 14px;overflow: hidden;text-overflow: ellipsis;word-wrap:break-word;word-break: break-all;}
        </style>
        <script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
        <script type="text/javascript">
            var c;
            function execCopy(event,thisDiv){
                event.preventDefault();
                if (event.clipboardData) {
                    event.clipboardData.setData("text/plain", thisDiv.innerHTML.replace(/&amp;/g,"%26"));
                    c=thisDiv.innerHTML;
                }
                thisDiv.innerHTML = "复制成功";
                setTimeout(function(){
                    thisDiv.innerHTML = c;
                },300);
            }

            function execClick(){
                document.execCommand("copy");
            }

            function hover(myID){
                myID.title = myID.innerHTML;
            }

            function find_div_length(){
                var div_length_right = $(".example_Con").length;
                var div_length_error = $(".example_Con2").length;
                var div_length = div_length_right + div_length_error;
                var correct_rate = div_length_right/div_length*100 + "%";
                $(".gk_three_").html(correct_rate);

                if (div_length_error > 0){
                    $("#test_status").html("有异常")
                    $("#test_status").css("background-color","red")
                }
                else{
                    $("#test_status").html("通过")
                    $("#test_status").css("background-color","#7FFFAA")
                }
            }
            $(document).ready(find_div_length);
        </script>
    </head>
    <body>
        <article>
            <header>
                <div class="heading">
                    <h3>测试报告（<span id="test_status">无异常</span>）</h3>
                    <div id="heading_r">
                        <div style="float:left;">执行人：
                            <span id="recipients">null</span></div>
                        <div style="float:right;width:300px;">执行日期：
                            <span id="data_send">"""
    html += str(now_time)
    html += """            </span></div>
                    </div>
                </div>
                <div class="heading_">
                    <div class="heading_t">
                        <h2>测试报告</h2>
                    </div>
                    <div class="heading_b"></div>
                </div>
            </header>
            <section>
                <!-- 概况 -->
                <p id="gk">&nbsp;&nbsp;<b>概况</b></p>
                <div class="gk">
                    <div class="gk_one">CGI平均响应时间（ms）</div>
                    <div class="gk_two">xxxxx（ms）</div>
                    <div class="gk_three">正确率</div>
                    <div class="gk_one_">x</div>
                    <div class="gk_two_"></div>
                    <div class="gk_three_"></div>
                </div>
                <!-- 接口测试用例执行详情 -->
                <p id="example">&nbsp;&nbsp;<b>接口测试用例执行详情</b></p>
                <div class="example">
                    <!-- 返回参数 -->
                    <div class="example_sub">No(序号)</div>
                    <div class="example_sub">title</div>
                    <div class="example_sub">url</div>
                    <div class="example_sub">state(状态码)</div>
                    <div class="example_sub">code</div>
                    <div class="example_sub">desc</div>
                    <div class="example_sub">result</div>
                    <div class="example_sub">分析结果</div>
                    <!-- 返回参数值 -->
                    """
    # 动态生成部分写在for循环里
    for test in data:
        if test[7] == "result返回完整" or test[7] == "数据返回成功" or test[7] == "返回的result是一个列表":
            if "异常" in test[1] and test[4] == 1:
                html = result_error(html, test)
                continue
            html = result_right(html, test)
        else:
            if "异常" in test[1] and test[4] != 1:
                html = result_right(html, test)
                continue
            html = result_error(html, test)
    html += """
                </div>
            </section>
        </article>
    </body>
    </html>
        """
    f.write(html.encode('utf-8'))
    f.close()
    webbrowser.open(GEN_HTML, new=0)


# 定义一个方法，当返回的数据与期望相同时，给表格加绿色背景显示
def result_right(html, test):
    html += '<div class="example_Con">'
    html += '   <div class="example_con" onmouseover="hover(this);">'+str(test[0])+'</div>'
    html += '</div>'
    html += '<div class="example_Con">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[1])+'</div>'
    html += '</div>'
    html += '<div class="example_Con">'
    html += '    <div id="copy" class="example_con" onclick="execClick()" oncopy="execCopy(event,this)">'+str(test[2])+'</div>'
    html += '</div>'
    html += '<div class="example_Con">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[3])+'</div>'
    html += '</div>'
    html += '<div class="example_Con">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[4])+'</div>'
    html += '</div>'
    html += '<div class="example_Con">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[5])+'</div>'
    html += '</div>'
    html += '<div class="example_Con">'
    html += '    <div class="example_con" onmouseover="hover(this);" onclick="execClick()" oncopy="execCopy(event,this)">'+str(test[6])+'</div>'
    html += '</div>'
    html += '<div class="example_Con">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[7])+'</div>'
    html += '</div>'
    return html


# 定义一个方法，当返回的数据与期望不符时，给表格加红色背景显示
def result_error(html, test):
    html += '<div class="example_Con2">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[0])+'</div>'
    html += '</div>'
    html += '<div class="example_Con2">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[1])+'</div>'
    html += '</div>'
    html += '<div class="example_Con2">'
    html += '    <div id="copy" class="example_con" onclick="execClick()" oncopy="execCopy(event,this)">'+str(test[2])+'</div>'
    html += '</div>'
    html += '<div class="example_Con2">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[3])+'</div>'
    html += '</div>'
    html += '<div class="example_Con2">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[4])+'</div>'
    html += '</div>'
    html += '<div class="example_Con2">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[5])+'</div>'
    html += '</div>'
    html += '<div class="example_Con2">'
    html += '    <div class="example_con" onmouseover="hover(this);" onclick="execClick()" oncopy="execCopy(event,this)">'+str(test[6])+'</div>'
    html += '</div>'
    html += '<div class="example_Con2">'
    html += '    <div class="example_con" onmouseover="hover(this);">'+str(test[7])+'</div>'
    html += '</div>'
    return html

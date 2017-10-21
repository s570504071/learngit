#coding=utf-8
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print data

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
con='''<!--周三-->
                <ul>
                    <li  class="tooltip" title="<h2>梦之祭！R</h2><p>偶像帅哥等你来收集</p>">
                        <div class="update-img">
                            <a href="/anime/dreamfestival2/" target="_blank">
                                <img src="/uploads/allimg/170824/6_1401539481.jpg" alt="梦之祭！R">
                                <p>第4话</p>
                                                                      
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/dreamfestival2/" target="_blank">梦之祭！R</a></h4>
                            <p>更新：第4话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>捏造TRAP–NTR</h2><p>你的老婆被女生抢走了！</p>">
                        <div class="update-img">
                            <a href="/anime/trapntr/" target="_blank">
                                <img src="/uploads/allimg/170628/6_1526127921.jpg" alt="捏造TRAP–NTR">
                                <p>第11话</p>
                                                                    
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/trapntr/" target="_blank">捏造TRAP–NTR</a></h4>
                            <p>更新：第11话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>武藏君和村山同学开始交往了</h2><p>武藏君和村山同学开始交往了动画全集武藏君和村山同学交往的日子。</p>">
                        <div class="update-img">
                            <a href="/anime/wtjhcstxksjwl/" target="_blank">
                                <img src="/uploads/allimg/170719/6_1436061001.jpg" alt="武藏君和村山同学开始交往了">
                                <p>第1话</p>
 
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/wtjhcstxksjwl/" target="_blank">武藏君和村山同学开始交往了</a></h4>
                            <p>更新：第1话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>猜谜王</h2><p>讲述高中一年级生越山识，刚刚入学就遭到了「quiz研」的奇怪学长会长劝说入会。被同级生真理强拉硬扯，内向的书虫越山识，一脚踏进了争夺0.1秒抢答的quiz世界。</p>">
                        <div class="update-img">
                            <a href="/anime/cmking/" target="_blank">
                                <img src="/uploads/allimg/170628/6_1459568642.jpg" alt="猜谜王">
                                <p>猜谜王</p>
                                                
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/cmking/" target="_blank">猜谜王</a></h4>
                            <p>更新：第11话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>最游记 第四季</h2><p>阻挡在三藏一行人面前的，五百年前的悲哀因缘……。</p>">

                        <div class="update-img">
                            <a href="/anime/zuiyouji4/" target="_blank">
                                <img src="/uploads/allimg/170628/6_1526126414.jpg" alt="最游记 第四季">
                                <p>最游记 第四季</p>
                                                                         
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/zuiyouji4/" target="_blank">最游记 第四季</a></h4>
                            <p>更新：第11话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>女高网球部 第九季</h2><p>基本不打网球的网球动漫。。</p>">
                        <div class="update-img">
                            <a href="/anime/tingqiushedjj/" target="_blank">
                                <img src="/uploads/allimg/170628/6_1526126005.jpg" alt="女高网球部 第九季">
                                <p>女高网球部 第九季</p>
                                                            
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/tingqiushedjj/" target="_blank">女高网球部 第九季</a></h4>
                            <p>更新：第10话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>第一次的辣妹</h2><p>莫名其妙和巨乳妹子交往了？？？</p>">
                        <div class="update-img">
                            <a href="/anime/lamei/" target="_blank">
                                <img src="/uploads/allimg/170628/6_1526248191.jpg" alt="第一次的辣妹">
                                <p>第一次的辣妹</p>
                                           
                             </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/lamei/" target="_blank">第一次的辣妹</a></h4>
                            <p>更新：第10话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>美男战国</h2><p>我的名字是佐助。原本是个研究生，但某天却穿越到了战国时代。而且，还是和在教科书里学到的历史完全不同的战国时代…</p>">

                        <div class="update-img">
                            <a href="/anime/mnzgcyskqwmksla/" target="_blank">
                                <img src="/uploads/allimg/170628/6_1526247383.jpg" alt="美男战国">
                                <p>第10话</p>
                                                                            
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/mnzgcyskqwmksla/" target="_blank">美男战国</a></h4>
                            <p>更新：第10话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>博人传</h2><p>七代目火影漩涡鸣人治理的木叶村。那是经历了战争的历史之后人们讴歌和平的时代。但是鸣人与其儿子漩涡博人的关系却并不和平…</p>">
                        <div class="update-img">
                            <a href="/anime/boruto/" target="_blank">
                                <img src="/uploads/allimg/170329/1_1629215932.jpg" alt="博人传">
                                <p>boruto</p>
                                  
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/boruto/" target="_blank">博人传</a></h4>
                            <p>第24话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>口水三国2</h2><p>画风Q萌，配音犀利，还伴随着各种作死方式</p>">
                        <div class="update-img">
                            <a href="/anime/kssg2/" target="_blank">
                                <img src="/uploads/allimg/170606/6_1126151071.jpg" alt="口水三国2">
                                <p>第22话</p>
                                   
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/kssg2/" target="_blank">口水三国2</a></h4>
                            <p>更新：第22话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>无责任银河 泰勒</h2><p>捡垃圾的班卓·植木·泰勒不知不觉拯救了被冰封在破烂宇宙船你的少女·戈萨168世（阿萨琳），两人为了复兴银河共和国踏上了旅行。</p>">
                        <div class="update-img">
                            <a href="/anime/wzryhtr/" target="_blank">
                                <img src="/uploads/allimg/170819/290_1146062711.jpg" alt="无责任银河 泰勒">
                                <p>无责任银河 泰勒</p>
                                    
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/wzryhtr/" target="_blank">无责任银河 泰勒</a></h4>
                            <p>第9话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>野良和皇女和野猫之心</h2><p>反田ノラ（野良）是一个和母亲收养的比自己小的夕莉シャチ一起生活的男生。虽然他们的母亲已经去世、没有双亲照顾，托周围的照顾，两人还是健康地成长着。</p>">
                        <div class="update-img">
                            <a href="/anime/yemao/" target="_blank">
                                <img src="/uploads/allimg/170819/290_1153332891.jpg" alt="野良和皇女和野猫之心">
                                <p>野良和皇女和野猫之心</p>
                                       
                             </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/yemao/" target="_blank">野良和皇女和野猫之心</a></h4>
                            <p>第10话</p>
                        </div>
                    </li>
                    <li  class="tooltip" title="<h2>画江湖之杯莫停</h2><p>《画江湖之杯莫停》是《画江湖》系列的第三部作品。</p>">
                        <div class="update-img">
                            <a href="/anime/hjhzbmt/" target="_blank">
                                <img src="http://static.jfrft.com/uploads/allimg/161110/1_1014568411.jpg" alt="画江湖之杯莫停">
                                <p>人未尽，杯莫停</p>
                                 
                            </a>
                        </div>
                        <div class="update-content">
                            <h4><a href="/anime/hjhzbmt/" target="_blank">画江湖之杯莫停</a></h4>
                            <p>第40话</p>
                        </div>
                    </li>
                </ul>'''

parser.feed(con)


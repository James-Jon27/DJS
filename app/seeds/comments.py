from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text


def seed_comments():
    on = Comment(user_id=1, image_id=6, comment="I think ginger is a wonderful root!")
    tw = Comment(
        user_id=1,
        image_id=7,
        comment="No soul (My apologies to any future ginger employer)",
    )
    th = Comment(
        user_id=1, image_id=4, comment="What's your email, I'd love a few recipes"
    )
    fo = Comment(
        user_id=1, image_id=11, comment="I wonder if coding is fun, I should pick it up"
    )
    fi = Comment(
        user_id=2,
        image_id=10,
        comment="I don't think your title accurately describes what this code block does",
    )
    si = Comment(
        user_id=2, image_id=11, comment="You forgot how much i pull out my hair :P"
    )
    se = Comment(user_id=2, image_id=2, comment="THEEE ROOOOOOOOOOKKKKKK")
    ei = Comment(user_id=3, image_id=2, comment="THEEEE ROOOOOOOOKKKKKKK")
    ni = Comment(user_id=3, image_id=1, comment="He sac'd the queen!")
    te = Comment(
        user_id=3, image_id=5, comment="I din't know ginger had so many benefits"
    )
    comment1 = Comment(user_id=3, image_id=45, comment="This is amazing!")
    comment2 = Comment(user_id=5, image_id=12, comment="Such a vibrant color palette!")
    comment3 = Comment(user_id=1, image_id=78, comment="Absolutely gorgeous!")
    comment4 = Comment(user_id=4, image_id=33, comment="Beautiful shot!")
    comment5 = Comment(user_id=7, image_id=101, comment="What a great perspective!")
    comment6 = Comment(user_id=2, image_id=67, comment="Incredible detail!")
    comment7 = Comment(user_id=6, image_id=90, comment="Wow, just wow!")
    comment8 = Comment(user_id=2, image_id=56, comment="This tells a story!")
    comment9 = Comment(user_id=1, image_id=15, comment="This made my day!")
    comment10 = Comment(
        user_id=3, image_id=34, comment="You have a great eye for photography!"
    )
    comment11 = Comment(user_id=5, image_id=21, comment="This is pure art!")
    comment12 = Comment(user_id=4, image_id=50, comment="I can't get enough of this!")
    comment13 = Comment(user_id=6, image_id=11, comment="So inspiring!")
    comment14 = Comment(user_id=2, image_id=88, comment="This is breathtaking!")
    comment15 = Comment(user_id=1, image_id=73, comment="A fantastic capture!")
    comment16 = Comment(user_id=7, image_id=99, comment="Stunning work!")
    comment17 = Comment(user_id=3, image_id=14, comment="This is so creative!")
    comment18 = Comment(user_id=5, image_id=84, comment="You nailed it!")
    comment19 = Comment(user_id=6, image_id=7, comment="Wow, just wow!")
    comment20 = Comment(user_id=2, image_id=47, comment="This made my day!")
    comment21 = Comment(user_id=4, image_id=19, comment="Incredible detail!")
    comment22 = Comment(user_id=1, image_id=60, comment="Such a vibrant color palette!")
    comment23 = Comment(user_id=7, image_id=27, comment="Absolutely gorgeous!")
    comment24 = Comment(user_id=3, image_id=68, comment="This tells a story!")
    comment25 = Comment(user_id=5, image_id=92, comment="Stunning work!")
    comment26 = Comment(user_id=6, image_id=3, comment="This is amazing!")
    comment27 = Comment(user_id=1, image_id=85, comment="Wow, just wow!")
    comment28 = Comment(
        user_id=4, image_id=41, comment="You have a great eye for photography!"
    )
    comment29 = Comment(user_id=2, image_id=76, comment="This is breathtaking!")
    comment30 = Comment(user_id=3, image_id=5, comment="What a great perspective!")
    comment31 = Comment(user_id=7, image_id=95, comment="Absolutely gorgeous!")
    comment32 = Comment(user_id=5, image_id=31, comment="Beautiful shot!")
    comment33 = Comment(user_id=6, image_id=55, comment="A fantastic capture!")
    comment34 = Comment(user_id=1, image_id=40, comment="So inspiring!")
    comment35 = Comment(user_id=4, image_id=83, comment="This is pure art!")
    comment36 = Comment(user_id=2, image_id=2, comment="This is so creative!")
    comment37 = Comment(user_id=3, image_id=70, comment="Absolutely gorgeous!")
    comment38 = Comment(user_id=5, image_id=37, comment="This made my day!")
    comment39 = Comment(user_id=6, image_id=48, comment="Wow, just wow!")
    comment40 = Comment(user_id=7, image_id=53, comment="Incredible detail!")
    comment41 = Comment(user_id=1, image_id=88, comment="Such a vibrant color palette!")
    comment42 = Comment(user_id=2, image_id=20, comment="You nailed it!")
    comment43 = Comment(user_id=3, image_id=62, comment="This tells a story!")
    comment44 = Comment(user_id=4, image_id=77, comment="This is amazing!")
    comment45 = Comment(user_id=5, image_id=10, comment="This is breathtaking!")
    comment46 = Comment(user_id=6, image_id=36, comment="What a great perspective!")
    comment47 = Comment(user_id=7, image_id=100, comment="Absolutely gorgeous!")
    comment48 = Comment(user_id=1, image_id=71, comment="Stunning work!")
    comment49 = Comment(user_id=2, image_id=29, comment="This is so creative!")
    comment50 = Comment(user_id=3, image_id=42, comment="So inspiring!")
    comment51 = Comment(user_id=4, image_id=8, comment="This tells a story!")
    comment52 = Comment(user_id=5, image_id=44, comment="Wow, just wow!")
    comment53 = Comment(
        user_id=6, image_id=13, comment="You have a great eye for photography!"
    )
    comment54 = Comment(user_id=7, image_id=65, comment="This is pure art!")
    comment55 = Comment(user_id=1, image_id=93, comment="Incredible detail!")
    comment56 = Comment(user_id=2, image_id=49, comment="Beautiful shot!")
    comment57 = Comment(user_id=3, image_id=61, comment="This made my day!")
    comment58 = Comment(user_id=4, image_id=39, comment="A fantastic capture!")
    comment59 = Comment(user_id=5, image_id=58, comment="This is breathtaking!")
    comment60 = Comment(user_id=6, image_id=72, comment="Absolutely gorgeous!")
    comment61 = Comment(user_id=1, image_id=64, comment="What a great perspective!")
    comment62 = Comment(user_id=2, image_id=12, comment="You nailed it!")
    comment63 = Comment(user_id=3, image_id=25, comment="This is amazing!")
    comment64 = Comment(user_id=4, image_id=87, comment="This tells a story!")
    comment65 = Comment(user_id=5, image_id=30, comment="Incredible detail!")
    comment66 = Comment(user_id=6, image_id=59, comment="So inspiring!")
    comment67 = Comment(user_id=7, image_id=97, comment="Wow, just wow!")
    comment68 = Comment(user_id=1, image_id=9, comment="This is pure art!")
    comment69 = Comment(user_id=2, image_id=17, comment="This is breathtaking!")
    comment70 = Comment(user_id=3, image_id=54, comment="Stunning work!")
    comment71 = Comment(user_id=4, image_id=32, comment="Absolutely gorgeous!")
    comment72 = Comment(user_id=5, image_id=46, comment="Wow, just wow!")
    comment73 = Comment(user_id=6, image_id=38, comment="You have a great eye for photography!")
    comment74 = Comment(user_id=7, image_id=74, comment="This tells a story!")
    comment75 = Comment(user_id=1, image_id=80, comment="This is amazing!")
    comment76 = Comment(user_id=2, image_id=8, comment="What a great perspective!")
    comment77 = Comment(user_id=3, image_id=91, comment="This made my day!")
    comment78 = Comment(user_id=4, image_id=66, comment="You nailed it!")
    comment79 = Comment(user_id=5, image_id=35, comment="So inspiring!")
    comment80 = Comment(user_id=3, image_id=12, comment="Absolutely stunning!")
    comment81 = Comment(user_id=7, image_id=45, comment="I love this perspective!")
    comment82 = Comment(user_id=2, image_id=78, comment="Such a beautiful scene!")
    comment83 = Comment(user_id=4, image_id=29, comment="Incredible detail!")
    comment84 = Comment(user_id=1, image_id=50, comment="This makes me smile!")
    comment85 = Comment(user_id=6, image_id=3, comment="A masterpiece!")
    comment86 = Comment(user_id=5, image_id=61, comment="Wow, just wow!")
    comment87 = Comment(user_id=3, image_id=90, comment="This is pure art!")
    comment88 = Comment(user_id=7, image_id=14, comment="I'm in love with this!")
    comment89 = Comment(user_id=2, image_id=37, comment="What a great shot!")
    comment90 = Comment(user_id=4, image_id=58, comment="Such vibrant colors!")
    comment91 = Comment(user_id=1, image_id=69, comment="This is breathtaking!")
    comment92 = Comment(user_id=6, image_id=22, comment="Love the composition!")
    comment93 = Comment(user_id=5, image_id=11, comment="Perfectly captured!")
    comment94 = Comment(user_id=3, image_id=80, comment="So much emotion here!")
    comment95 = Comment(user_id=7, image_id=23, comment="Absolutely beautiful!")
    comment96 = Comment(user_id=2, image_id=32, comment="This speaks to me!")
    comment97 = Comment(user_id=4, image_id=76, comment="Fantastic work!")
    comment98 = Comment(user_id=1, image_id=19, comment="So inspiring!")
    comment99 = Comment(user_id=6, image_id=41, comment="A great find!")
    comment100 = Comment(user_id=5, image_id=53, comment="Stunning colors!")
    comment101 = Comment(user_id=3, image_id=87, comment="I could look at this all day!")
    comment102 = Comment(user_id=7, image_id=18, comment="This is so calming!")
    comment103 = Comment(user_id=2, image_id=34, comment="The lighting is perfect!")
    comment104 = Comment(user_id=4, image_id=65, comment="Simply gorgeous!")
    comment105 = Comment(user_id=1, image_id=39, comment="A visual treat!")
    comment106 = Comment(user_id=6, image_id=42, comment="Wow, just amazing!")
    comment107 = Comment(user_id=5, image_id=30, comment="This made my day!")
    comment108 = Comment(user_id=3, image_id=9, comment="Truly inspiring work!")
    comment109 = Comment(user_id=7, image_id=16, comment="Such a great view!")
    comment110 = Comment(user_id=2, image_id=54, comment="I love this artwork!")
    comment111 = Comment(user_id=4, image_id=70, comment="Absolutely mesmerizing!")
    comment112 = Comment(user_id=1, image_id=48, comment="This is so unique!")
    comment113 = Comment(user_id=6, image_id=25, comment="Incredible use of color!")
    comment114 = Comment(user_id=5, image_id=59, comment="Love the texture!")
    comment115 = Comment(user_id=3, image_id=15, comment="Such a captivating image!")
    comment116 = Comment(user_id=7, image_id=33, comment="This is breathtaking!")
    comment117 = Comment(user_id=2, image_id=46, comment="An amazing perspective!")
    comment118 = Comment(user_id=4, image_id=62, comment="What a beautiful moment!")
    comment119 = Comment(user_id=1, image_id=77, comment="Pure elegance!")
    comment120 = Comment(user_id=6, image_id=8, comment="Love the contrast!")
    comment121 = Comment(user_id=5, image_id=20, comment="This is so refreshing!")
    comment122 = Comment(user_id=3, image_id=26, comment="The beauty of nature!")
    comment123 = Comment(user_id=7, image_id=49, comment="What a fantastic capture!")
    comment124 = Comment(user_id=2, image_id=74, comment="This brings me joy!")
    comment125 = Comment(user_id=4, image_id=13, comment="So much talent on display!")
    comment126 = Comment(user_id=1, image_id=60, comment="A perfect shot!")
    comment127 = Comment(user_id=6, image_id=36, comment="Such creativity!")
    comment128 = Comment(user_id=5, image_id=55, comment="This image tells a story!")
    comment129 = Comment(user_id=3, image_id=7, comment="Love the details here!")
    comment130 = Comment(user_id=7, image_id=24, comment="So artistic!")
    comment131 = Comment(user_id=2, image_id=44, comment="Incredible framing!")
    comment132 = Comment(user_id=4, image_id=75, comment="This is a true gem!")
    comment133 = Comment(user_id=1, image_id=88, comment="What a delightful view!")
    comment134 = Comment(user_id=6, image_id=12, comment="Absolutely gorgeous!")
    comment135 = Comment(user_id=5, image_id=66, comment="This is so enchanting!")
    comment136 = Comment(user_id=3, image_id=31, comment="I can't get enough of this!")
    comment137 = Comment(user_id=7, image_id=47, comment="So beautiful and serene!")
    comment138 = Comment(user_id=2, image_id=11, comment="This image is captivating!")
    comment139 = Comment(user_id=4, image_id=82, comment="What an incredible find!")
    comment140 = Comment(user_id=1, image_id=91, comment="Such a charming image!")
    comment141 = Comment(user_id=6, image_id=57, comment="This brings me peace!")
    comment142 = Comment(user_id=5, image_id=84, comment="Amazing clarity!")
    comment143 = Comment(user_id=3, image_id=40, comment="This is so eye-catching!")
    comment144 = Comment(user_id=7, image_id=21, comment="What a striking photo!")
    comment145 = Comment(user_id=2, image_id=73, comment="Such a lovely moment captured!")
    comment146 = Comment(user_id=4, image_id=97, comment="So uplifting!")
    comment147 = Comment(user_id=1, image_id=10, comment="This is truly special!")
    comment148 = Comment(user_id=6, image_id=68, comment="I adore this!")
    comment149 = Comment(user_id=5, image_id=85, comment="Such a fantastic composition!")
    comment150 = Comment(user_id=3, image_id=29, comment="What a magnificent view!")
    comment151 = Comment(user_id=7, image_id=56, comment="This makes me happy!")
    comment152 = Comment(user_id=2, image_id=94, comment="Such a great representation of nature!")
    comment153 = Comment(user_id=4, image_id=15, comment="Absolutely breathtaking scenery!")
    comment154 = Comment(user_id=1, image_id=72, comment="This is a stunning capture!")
    comment155 = Comment(user_id=6, image_id=83, comment="So charming and inviting!")
    comment156 = Comment(user_id=5, image_id=35, comment="What a creative shot!")
    comment157 = Comment(user_id=3, image_id=63, comment="Incredible artistry!")
    comment158 = Comment(user_id=7, image_id=92, comment="Such beautiful imagery!")
    comment159 = Comment(user_id=2, image_id=41, comment="This artwork is so vibrant!")
    comment160 = Comment(user_id=4, image_id=99, comment="An absolute treasure!")
    comment161 = Comment(user_id=4, image_id=27, comment="This is simply beautiful!")
    comment162 = Comment(user_id=2, image_id=88, comment="Such a wonderful capture!")
    comment163 = Comment(user_id=1, image_id=19, comment="Absolutely love this!")
    comment164 = Comment(user_id=6, image_id=72, comment="What an amazing shot!")
    comment165 = Comment(user_id=5, image_id=45, comment="This is breathtaking!")
    comment166 = Comment(user_id=3, image_id=33, comment="So much creativity!")
    comment167 = Comment(user_id=7, image_id=50, comment="Incredible view!")
    comment168 = Comment(user_id=4, image_id=66, comment="This makes me smile!")
    comment169 = Comment(user_id=2, image_id=10, comment="A perfect picture!")
    comment170 = Comment(user_id=1, image_id=73, comment="Such vibrant colors!")
    comment171 = Comment(user_id=6, image_id=31, comment="This is truly inspiring!")
    comment172 = Comment(user_id=5, image_id=24, comment="Absolutely stunning work!")
    comment173 = Comment(user_id=3, image_id=12, comment="Love the details!")
    comment174 = Comment(user_id=7, image_id=85, comment="This is so enchanting!")
    comment175 = Comment(user_id=4, image_id=57, comment="Such a delightful view!")
    comment176 = Comment(user_id=2, image_id=29, comment="This is a masterpiece!")
    comment177 = Comment(user_id=1, image_id=8, comment="I can't stop looking at this!")
    comment178 = Comment(user_id=6, image_id=44, comment="Such a unique perspective!")
    comment179 = Comment(user_id=5, image_id=93, comment="What a fantastic find!")
    comment180 = Comment(user_id=3, image_id=68, comment="This captures the moment perfectly!")
    comment181 = Comment(user_id=7, image_id=15, comment="So calming and peaceful!")
    comment182 = Comment(user_id=4, image_id=39, comment="This is pure joy!")
    comment183 = Comment(user_id=2, image_id=62, comment="Incredible artistry!")
    comment184 = Comment(user_id=1, image_id=27, comment="What a beautiful piece!")
    comment185 = Comment(user_id=6, image_id=78, comment="Such a great use of color!")
    comment186 = Comment(user_id=5, image_id=4, comment="Absolutely breathtaking scenery!")
    comment187 = Comment(user_id=3, image_id=71, comment="This makes my heart happy!")
    comment188 = Comment(user_id=7, image_id=54, comment="Love the lighting in this!")
    comment189 = Comment(user_id=4, image_id=99, comment="What an amazing capture!")
    comment190 = Comment(user_id=2, image_id=21, comment="This is so delightful!")
    comment191 = Comment(user_id=1, image_id=86, comment="Such a creative shot!")
    comment192 = Comment(user_id=6, image_id=11, comment="A wonderful interpretation!")
    comment193 = Comment(user_id=5, image_id=47, comment="Such rich colors!")
    comment194 = Comment(user_id=3, image_id=96, comment="This is absolutely stunning!")
    comment195 = Comment(user_id=7, image_id=22, comment="So much emotion in this!")
    comment196 = Comment(user_id=4, image_id=34, comment="This is simply magical!")
    comment197 = Comment(user_id=2, image_id=13, comment="What a lovely scene!")
    comment198 = Comment(user_id=1, image_id=90, comment="Such a fantastic moment captured!")
    comment199 = Comment(user_id=6, image_id=30, comment="This artwork is captivating!")
    comment200 = Comment(user_id=5, image_id=49, comment="So inviting and warm!")
    comment201 = Comment(user_id=3, image_id=38, comment="Such a great shot!")
    comment202 = Comment(user_id=7, image_id=82, comment="Absolutely mesmerizing!")
    comment203 = Comment(user_id=4, image_id=5, comment="What a great perspective!")
    comment204 = Comment(user_id=2, image_id=74, comment="Incredible work!")
    comment205 = Comment(user_id=1, image_id=16, comment="This brings back memories!")
    comment206 = Comment(user_id=6, image_id=40, comment="Such an inspiring image!")
    comment207 = Comment(user_id=5, image_id=67, comment="What a joyful capture!")
    comment208 = Comment(user_id=3, image_id=53, comment="Love this artwork!")
    comment209 = Comment(user_id=7, image_id=1, comment="So refreshing!")
    comment210 = Comment(user_id=4, image_id=92, comment="This makes me smile!")
    comment211 = Comment(user_id=2, image_id=39, comment="What a lovely image!")
    comment212 = Comment(user_id=1, image_id=81, comment="Incredible perspective!")
    comment213 = Comment(user_id=6, image_id=59, comment="Such beauty in simplicity!")
    comment214 = Comment(user_id=5, image_id=8, comment="So calming to look at!")
    comment215 = Comment(user_id=3, image_id=10, comment="What a delightful capture!")
    comment216 = Comment(user_id=7, image_id=36, comment="This is so charming!")
    comment217 = Comment(user_id=4, image_id=14, comment="Absolutely beautiful!")
    comment218 = Comment(user_id=2, image_id=65, comment="Such vibrant imagery!")
    comment219 = Comment(user_id=1, image_id=23, comment="So much character!")
    comment220 = Comment(user_id=6, image_id=94, comment="Incredible detail and color!")
    comment221 = Comment(user_id=5, image_id=95, comment="Such a wonderful piece!")
    comment222 = Comment(user_id=3, image_id=77, comment="This is stunning!")
    comment223 = Comment(user_id=7, image_id=3, comment="What a remarkable view!")
    comment224 = Comment(user_id=4, image_id=70, comment="This brings me joy!")
    comment225 = Comment(user_id=2, image_id=48, comment="Such a great capture!")
    comment226 = Comment(user_id=1, image_id=63, comment="Love the mood in this!")
    comment227 = Comment(user_id=6, image_id=75, comment="What a striking image!")
    comment228 = Comment(user_id=5, image_id=32, comment="Absolutely lovely!")
    comment229 = Comment(user_id=3, image_id=17, comment="This image is captivating!")
    comment230 = Comment(user_id=7, image_id=25, comment="So unique and beautiful!")
    comment231 = Comment(user_id=4, image_id=56, comment="Incredible capture!")
    comment232 = Comment(user_id=2, image_id=99, comment="What an artistic view!")
    comment233 = Comment(user_id=1, image_id=41, comment="This image tells a story!")
    comment234 = Comment(user_id=6, image_id=6, comment="Such a heartwarming scene!")
    comment235 = Comment(user_id=5, image_id=80, comment="So inspiring and uplifting!")
    comment236 = Comment(user_id=3, image_id=4, comment="This is a work of art!")
    comment237 = Comment(user_id=7, image_id=83, comment="What an amazing shot!")
    comment238 = Comment(user_id=4, image_id=20, comment="Such a delightful image!")
    comment239 = Comment(user_id=2, image_id=91, comment="This brings back so many memories!")
    comment240 = Comment(user_id=1, image_id=42, comment="Absolutely stunning work!")
    comment241 = Comment(user_id=3, image_id=26, comment="Absolutely stunning!")
    comment242 = Comment(user_id=7, image_id=65, comment="Such a beautiful moment!")
    comment243 = Comment(user_id=1, image_id=49, comment="This makes me smile!")
    comment244 = Comment(user_id=4, image_id=18, comment="Incredible work of art!")
    comment245 = Comment(user_id=2, image_id=78, comment="What a captivating scene!")
    comment246 = Comment(user_id=5, image_id=92, comment="So inspiring!")
    comment247 = Comment(user_id=6, image_id=13, comment="This is simply magical!")
    comment248 = Comment(user_id=3, image_id=62, comment="Love the colors!")
    comment249 = Comment(user_id=7, image_id=11, comment="Such a great shot!")
    comment250 = Comment(user_id=1, image_id=84, comment="What an amazing view!")
    comment251 = Comment(user_id=4, image_id=56, comment="So much creativity!")
    comment252 = Comment(user_id=2, image_id=31, comment="This brings joy!")
    comment253 = Comment(user_id=5, image_id=77, comment="Absolutely love this!")
    comment254 = Comment(user_id=6, image_id=40, comment="So calming and peaceful!")
    comment255 = Comment(user_id=3, image_id=9, comment="What a delightful capture!")
    comment256 = Comment(user_id=7, image_id=85, comment="Such a unique perspective!")
    comment257 = Comment(user_id=1, image_id=22, comment="This is breathtaking!")
    comment258 = Comment(user_id=4, image_id=53, comment="What a lovely image!")
    comment259 = Comment(user_id=2, image_id=99, comment="Such vibrant colors!")
    comment260 = Comment(user_id=5, image_id=39, comment="This is truly inspiring!")
    comment261 = Comment(user_id=6, image_id=68, comment="Such rich details!")
    comment262 = Comment(user_id=3, image_id=25, comment="Incredible capture!")
    comment263 = Comment(user_id=7, image_id=72, comment="Love this artwork!")
    comment264 = Comment(user_id=1, image_id=4, comment="What a fantastic find!")
    comment265 = Comment(user_id=4, image_id=57, comment="So much emotion in this!")
    comment266 = Comment(user_id=2, image_id=46, comment="This is simply beautiful!")
    comment267 = Comment(user_id=5, image_id=88, comment="What a fantastic shot!")
    comment268 = Comment(user_id=6, image_id=64, comment="Absolutely mesmerizing!")
    comment269 = Comment(user_id=3, image_id=12, comment="Such beauty in simplicity!")
    comment270 = Comment(user_id=7, image_id=30, comment="This is so enchanting!")
    comment271 = Comment(user_id=1, image_id=70, comment="So inviting and warm!")
    comment272 = Comment(user_id=4, image_id=35, comment="Such a great perspective!")
    comment273 = Comment(user_id=2, image_id=16, comment="Incredible artistry!")
    comment274 = Comment(user_id=5, image_id=21, comment="This makes my heart happy!")
    comment275 = Comment(user_id=6, image_id=87, comment="So inspiring and uplifting!")
    comment276 = Comment(user_id=3, image_id=73, comment="What an artistic view!")
    comment277 = Comment(user_id=7, image_id=19, comment="Such a delightful image!")
    comment278 = Comment(user_id=1, image_id=10, comment="What an amazing moment captured!")
    comment279 = Comment(user_id=4, image_id=90, comment="This artwork is captivating!")
    comment280 = Comment(user_id=2, image_id=37, comment="Such a unique and beautiful image!")
    comment281 = Comment(user_id=5, image_id=58, comment="So much character!")
    comment282 = Comment(user_id=6, image_id=81, comment="Absolutely stunning work!")
    comment283 = Comment(user_id=3, image_id=75, comment="What a wonderful interpretation!")
    comment284 = Comment(user_id=7, image_id=8, comment="This is pure joy!")
    comment285 = Comment(user_id=1, image_id=66, comment="So much creativity in this shot!")
    comment286 = Comment(user_id=4, image_id=17, comment="What a lovely piece!")
    comment287 = Comment(user_id=2, image_id=44, comment="Such a beautiful landscape!")
    comment288 = Comment(user_id=5, image_id=91, comment="This is a work of art!")
    comment289 = Comment(user_id=6, image_id=2, comment="Absolutely lovely capture!")
    comment290 = Comment(user_id=3, image_id=83, comment="So refreshing!")
    comment291 = Comment(user_id=7, image_id=34, comment="What an incredible shot!")
    comment292 = Comment(user_id=1, image_id=63, comment="So calming to look at!")
    comment293 = Comment(user_id=4, image_id=29, comment="Incredible detail and color!")
    comment294 = Comment(user_id=2, image_id=61, comment="Such a wonderful scene!")
    comment295 = Comment(user_id=5, image_id=74, comment="What a great capture!")
    comment296 = Comment(user_id=6, image_id=26, comment="This image tells a story!")
    comment297 = Comment(user_id=3, image_id=99, comment="So much emotion in this shot!")
    comment298 = Comment(user_id=7, image_id=55, comment="Such a fantastic moment!")
    comment299 = Comment(user_id=1, image_id=80, comment="What a breathtaking view!")
    comment300 = Comment(user_id=4, image_id=36, comment="Absolutely enchanting!")
    comment301 = Comment(user_id=2, image_id=69, comment="Such a unique composition!")
    comment302 = Comment(user_id=5, image_id=47, comment="This brings back so many memories!")
    comment303 = Comment(user_id=6, image_id=1, comment="Incredible capture of beauty!")
    comment304 = Comment(user_id=3, image_id=14, comment="So much joy in this image!")
    comment305 = Comment(user_id=7, image_id=93, comment="What an amazing scene!")
    comment306 = Comment(user_id=1, image_id=24, comment="Such vibrant imagery!")
    comment307 = Comment(user_id=4, image_id=7, comment="This makes me so happy!")
    comment308 = Comment(user_id=2, image_id=54, comment="What a lovely capture!")
    comment309 = Comment(user_id=5, image_id=63, comment="So much love in this image!")
    comment310 = Comment(user_id=6, image_id=10, comment="This is such a special moment!")
    comment311 = Comment(user_id=3, image_id=41, comment="What a beautiful landscape!")
    comment312 = Comment(user_id=7, image_id=86, comment="Incredible detail!")
    comment313 = Comment(user_id=1, image_id=43, comment="Absolutely stunning artwork!")
    comment314 = Comment(user_id=4, image_id=33, comment="So inviting and beautiful!")
    comment315 = Comment(user_id=2, image_id=15, comment="Such an enchanting view!")
    comment316 = Comment(user_id=5, image_id=67, comment="What a remarkable piece of art!")
    comment317 = Comment(user_id=6, image_id=60, comment="This is so charming!")
    comment318 = Comment(user_id=3, image_id=82, comment="What an incredible moment captured!")
    comment319 = Comment(user_id=7, image_id=3, comment="Such a delightful image!")
    comment320 = Comment(user_id=1, image_id=76, comment="This is simply beautiful!")
    comment321 = Comment(user_id=2, image_id=15, comment="Such a vibrant scene!")
    comment322 = Comment(user_id=4, image_id=48, comment="Absolutely stunning!")
    comment323 = Comment(user_id=1, image_id=91, comment="This makes me smile!")
    comment324 = Comment(user_id=5, image_id=63, comment="What a captivating moment!")
    comment325 = Comment(user_id=3, image_id=7, comment="Incredible work of art!")
    comment326 = Comment(user_id=6, image_id=55, comment="So inspiring!")
    comment327 = Comment(user_id=2, image_id=32, comment="This is simply magical!")
    comment328 = Comment(user_id=4, image_id=79, comment="Love the colors!")
    comment329 = Comment(user_id=1, image_id=12, comment="Such a great shot!")
    comment330 = Comment(user_id=5, image_id=85, comment="What an amazing view!")
    comment331 = Comment(user_id=3, image_id=20, comment="So much creativity!")
    comment332 = Comment(user_id=6, image_id=77, comment="This brings joy!")
    comment333 = Comment(user_id=2, image_id=38, comment="Absolutely love this!")
    comment334 = Comment(user_id=4, image_id=41, comment="So calming and peaceful!")
    comment335 = Comment(user_id=1, image_id=64, comment="What a delightful capture!")
    comment336 = Comment(user_id=5, image_id=9, comment="Such a unique perspective!")
    comment337 = Comment(user_id=3, image_id=69, comment="This is breathtaking!")
    comment338 = Comment(user_id=6, image_id=30, comment="What a lovely image!")
    comment339 = Comment(user_id=2, image_id=46, comment="Such vibrant colors!")
    comment340 = Comment(user_id=4, image_id=82, comment="This is truly inspiring!")
    comment341 = Comment(user_id=1, image_id=18, comment="Such rich details!")
    comment342 = Comment(user_id=5, image_id=74, comment="Incredible capture!")
    comment343 = Comment(user_id=3, image_id=14, comment="Love this artwork!")
    comment344 = Comment(user_id=6, image_id=66, comment="What a fantastic find!")
    comment345 = Comment(user_id=2, image_id=54, comment="So much emotion in this!")
    comment346 = Comment(user_id=4, image_id=8, comment="This image tells a story!")
    comment347 = Comment(user_id=1, image_id=49, comment="So inspiring and uplifting!")
    comment348 = Comment(user_id=5, image_id=21, comment="What a beautiful landscape!")
    comment349 = Comment(user_id=3, image_id=90, comment="This is so charming!")
    comment350 = Comment(user_id=6, image_id=53, comment="What an incredible moment captured!")
    comment351 = Comment(user_id=2, image_id=2, comment="So inviting and warm!")
    comment352 = Comment(user_id=4, image_id=43, comment="Such a great perspective!")
    comment353 = Comment(user_id=1, image_id=28, comment="Incredible artistry!")
    comment354 = Comment(user_id=5, image_id=11, comment="This makes my heart happy!")
    comment355 = Comment(user_id=3, image_id=80, comment="What a fantastic shot!")
    comment356 = Comment(user_id=6, image_id=60, comment="Absolutely mesmerizing!")
    comment357 = Comment(user_id=2, image_id=33, comment="So refreshing!")
    comment358 = Comment(user_id=4, image_id=78, comment="What an amazing scene!")
    comment359 = Comment(user_id=1, image_id=5, comment="So calming to look at!")
    comment360 = Comment(user_id=5, image_id=39, comment="Incredible detail and color!")
    comment361 = Comment(user_id=3, image_id=7, comment="Such a wonderful scene!")
    comment362 = Comment(user_id=6, image_id=65, comment="What a great capture!")
    comment363 = Comment(user_id=2, image_id=13, comment="This image brings peace!")
    comment364 = Comment(user_id=4, image_id=99, comment="Such a delightful image!")
    comment365 = Comment(user_id=1, image_id=17, comment="What a breathtaking view!")
    comment366 = Comment(user_id=5, image_id=27, comment="Absolutely enchanting!")
    comment367 = Comment(user_id=3, image_id=88, comment="Such a unique composition!")
    comment368 = Comment(user_id=6, image_id=19, comment="This brings back so many memories!")
    comment369 = Comment(user_id=2, image_id=42, comment="Incredible capture of beauty!")
    comment370 = Comment(user_id=4, image_id=96, comment="So much joy in this image!")
    comment371 = Comment(user_id=1, image_id=34, comment="What an amazing scene!")
    comment372 = Comment(user_id=5, image_id=29, comment="Such vibrant imagery!")
    comment373 = Comment(user_id=3, image_id=84, comment="This makes me so happy!")
    comment374 = Comment(user_id=6, image_id=22, comment="What a lovely capture!")
    comment375 = Comment(user_id=2, image_id=57, comment="So much love in this image!")
    comment376 = Comment(user_id=4, image_id=8, comment="This is such a special moment!")
    comment377 = Comment(user_id=1, image_id=100, comment="What a beautiful landscape!")
    comment378 = Comment(user_id=5, image_id=71, comment="Incredible detail!")
    comment379 = Comment(user_id=3, image_id=15, comment="Absolutely stunning artwork!")
    comment380 = Comment(user_id=6, image_id=23, comment="So inviting and beautiful!")
    comment381 = Comment(user_id=2, image_id=39, comment="Such an enchanting view!")
    comment382 = Comment(user_id=4, image_id=48, comment="What a remarkable piece of art!")
    comment383 = Comment(user_id=1, image_id=58, comment="This is so charming!")
    comment384 = Comment(user_id=5, image_id=12, comment="What an incredible moment captured!")
    comment385 = Comment(user_id=3, image_id=53, comment="Such beauty in simplicity!")
    comment386 = Comment(user_id=6, image_id=92, comment="This is pure joy!")
    comment387 = Comment(user_id=2, image_id=73, comment="So much creativity in this shot!")
    comment388 = Comment(user_id=4, image_id=37, comment="What a lovely piece!")
    comment389 = Comment(user_id=1, image_id=25, comment="Such a beautiful landscape!")
    comment390 = Comment(user_id=5, image_id=61, comment="This is a work of art!")
    comment391 = Comment(user_id=3, image_id=6, comment="Absolutely lovely capture!")
    comment392 = Comment(user_id=6, image_id=83, comment="So refreshing!")
    comment393 = Comment(user_id=2, image_id=44, comment="What an incredible shot!")
    comment394 = Comment(user_id=4, image_id=72, comment="So calming to look at!")
    comment395 = Comment(user_id=1, image_id=50, comment="Incredible detail and color!")
    comment396 = Comment(user_id=5, image_id=16, comment="Such a wonderful scene!")
    comment397 = Comment(user_id=3, image_id=69, comment="What a great capture!")
    comment398 = Comment(user_id=6, image_id=86, comment="Absolutely mesmerizing!")
    comment399 = Comment(user_id=2, image_id=38, comment="So much joy in this image!")
    comment400 = Comment(user_id=4, image_id=4, comment="This is simply beautiful!")
    comment401 = Comment(user_id=2, image_id=17, comment="This is so beautiful!")
    comment402 = Comment(user_id=4, image_id=88, comment="Absolutely stunning!")
    comment403 = Comment(user_id=1, image_id=53, comment="What an amazing capture!")
    comment404 = Comment(user_id=5, image_id=11, comment="Incredible work of art!")
    comment405 = Comment(user_id=3, image_id=22, comment="So inspiring!")
    comment406 = Comment(user_id=6, image_id=47, comment="Such a vibrant scene!")
    comment407 = Comment(user_id=2, image_id=36, comment="This makes me smile!")
    comment408 = Comment(user_id=4, image_id=92, comment="Love the colors!")
    comment409 = Comment(user_id=1, image_id=72, comment="Such a delightful capture!")
    comment410 = Comment(user_id=5, image_id=64, comment="What a captivating moment!")
    comment411 = Comment(user_id=3, image_id=10, comment="So much creativity!")
    comment412 = Comment(user_id=6, image_id=81, comment="What a lovely image!")
    comment413 = Comment(user_id=2, image_id=7, comment="This is simply magical!")
    comment414 = Comment(user_id=4, image_id=5, comment="Such rich details!")
    comment415 = Comment(user_id=1, image_id=39, comment="This image tells a story!")
    comment416 = Comment(user_id=5, image_id=29, comment="So calming and peaceful!")
    comment417 = Comment(user_id=3, image_id=60, comment="Such beauty in simplicity!")
    comment418 = Comment(user_id=6, image_id=44, comment="What an amazing view!")
    comment419 = Comment(user_id=2, image_id=66, comment="This brings joy!")
    comment420 = Comment(user_id=4, image_id=12, comment="Such a great perspective!")
    comment421 = Comment(user_id=1, image_id=90, comment="Incredible artistry!")
    comment422 = Comment(user_id=5, image_id=8, comment="What a fantastic find!")
    comment423 = Comment(user_id=3, image_id=59, comment="Absolutely love this!")
    comment424 = Comment(user_id=6, image_id=83, comment="What a breathtaking view!")
    comment425 = Comment(user_id=2, image_id=26, comment="So much emotion in this!")
    comment426 = Comment(user_id=4, image_id=42, comment="What an incredible moment captured!")
    comment427 = Comment(user_id=1, image_id=55, comment="This image brings peace!")
    comment428 = Comment(user_id=5, image_id=38, comment="What a beautiful landscape!")
    comment429 = Comment(user_id=3, image_id=99, comment="Such a unique composition!")
    comment430 = Comment(user_id=6, image_id=3, comment="So refreshing!")
    comment431 = Comment(user_id=2, image_id=14, comment="Incredible detail and color!")
    comment432 = Comment(user_id=4, image_id=30, comment="So inviting and warm!")
    comment433 = Comment(user_id=1, image_id=70, comment="Such a wonderful scene!")
    comment434 = Comment(user_id=5, image_id=75, comment="What a delightful image!")
    comment435 = Comment(user_id=3, image_id=18, comment="So calming to look at!")
    comment436 = Comment(user_id=6, image_id=23, comment="What an incredible shot!")
    comment437 = Comment(user_id=2, image_id=45, comment="This is pure joy!")
    comment438 = Comment(user_id=4, image_id=68, comment="Such a lovely piece!")
    comment439 = Comment(user_id=1, image_id=4, comment="What an incredible moment captured!")
    comment440 = Comment(user_id=5, image_id=19, comment="Absolutely mesmerizing!")
    comment441 = Comment(user_id=3, image_id=34, comment="This is such a special moment!")
    comment442 = Comment(user_id=6, image_id=40, comment="Such a beautiful landscape!")
    comment443 = Comment(user_id=2, image_id=33, comment="What a fantastic shot!")
    comment444 = Comment(user_id=4, image_id=58, comment="So much creativity in this shot!")
    comment445 = Comment(user_id=1, image_id=82, comment="This is so charming!")
    comment446 = Comment(user_id=5, image_id=31, comment="What an amazing capture!")
    comment447 = Comment(user_id=3, image_id=87, comment="So much joy in this image!")
    comment448 = Comment(user_id=6, image_id=24, comment="What a lovely capture!")
    comment449 = Comment(user_id=2, image_id=48, comment="So much love in this image!")
    comment450 = Comment(user_id=4, image_id=9, comment="This is simply beautiful!")
    comment451 = Comment(user_id=1, image_id=85, comment="What a remarkable piece of art!")
    comment452 = Comment(user_id=5, image_id=62, comment="Such beauty in simplicity!")
    comment453 = Comment(user_id=3, image_id=61, comment="What an incredible moment captured!")
    comment454 = Comment(user_id=6, image_id=74, comment="This makes my heart happy!")
    comment455 = Comment(user_id=2, image_id=15, comment="Such a unique perspective!")
    comment456 = Comment(user_id=4, image_id=37, comment="What a fantastic find!")
    comment457 = Comment(user_id=1, image_id=97, comment="This image brings peace!")
    comment458 = Comment(user_id=5, image_id=52, comment="Such a wonderful scene!")
    comment459 = Comment(user_id=3, image_id=73, comment="What a delightful image!")
    comment460 = Comment(user_id=6, image_id=91, comment="Incredible detail!")
    comment461 = Comment(user_id=2, image_id=56, comment="What a great capture!")
    comment462 = Comment(user_id=4, image_id=80, comment="So calming to look at!")
    comment463 = Comment(user_id=1, image_id=63, comment="So inspiring and uplifting!")
    comment464 = Comment(user_id=5, image_id=41, comment="What an amazing view!")
    comment465 = Comment(user_id=3, image_id=14, comment="This is pure joy!")
    comment466 = Comment(user_id=6, image_id=65, comment="So much creativity in this shot!")
    comment467 = Comment(user_id=2, image_id=93, comment="What a charming piece!")
    comment468 = Comment(user_id=4, image_id=69, comment="Absolutely enchanting!")
    comment469 = Comment(user_id=1, image_id=46, comment="Such an enchanting view!")
    comment470 = Comment(user_id=5, image_id=1, comment="What a lovely piece!")
    comment471 = Comment(user_id=3, image_id=50, comment="Such a unique composition!")
    comment472 = Comment(user_id=6, image_id=8, comment="This makes my heart happy!")
    comment473 = Comment(user_id=2, image_id=98, comment="What an incredible moment captured!")
    comment474 = Comment(user_id=4, image_id=83, comment="Such a delightful image!")
    comment475 = Comment(user_id=1, image_id=13, comment="What an amazing capture!")
    comment476 = Comment(user_id=5, image_id=35, comment="This image tells a story!")
    comment477 = Comment(user_id=3, image_id=20, comment="So refreshing!")
    comment478 = Comment(user_id=6, image_id=12, comment="Such a great perspective!")
    comment479 = Comment(user_id=2, image_id=76, comment="What a stunning view!")
    comment480 = Comment(user_id=4, image_id=2, comment="Absolutely mesmerizing!")
    comment481 = Comment(user_id=3, image_id=12, comment="Absolutely breathtaking!")
    comment482 = Comment(user_id=6, image_id=23, comment="I love this so much!")
    comment483 = Comment(user_id=2, image_id=45, comment="What a beautiful shot!")
    comment484 = Comment(user_id=4, image_id=34, comment="So inspiring!")
    comment485 = Comment(user_id=1, image_id=22, comment="Truly amazing work!")
    comment486 = Comment(user_id=5, image_id=50, comment="This makes me so happy!")
    comment487 = Comment(user_id=7, image_id=15, comment="A masterpiece!")
    comment488 = Comment(user_id=2, image_id=39, comment="Incredible!")
    comment489 = Comment(user_id=3, image_id=18, comment="Just wow!")
    comment490 = Comment(user_id=6, image_id=26, comment="I can't get enough of this!")
    comment491 = Comment(user_id=4, image_id=33, comment="What a fantastic perspective!")
    comment492 = Comment(user_id=1, image_id=48, comment="This is pure art!")
    comment493 = Comment(user_id=5, image_id=37, comment="So calming!")
    comment494 = Comment(user_id=7, image_id=42, comment="This is stunning!")
    comment495 = Comment(user_id=3, image_id=20, comment="Beautifully done!")
    comment496 = Comment(user_id=6, image_id=9, comment="I love the colors!")
    comment497 = Comment(user_id=4, image_id=30, comment="Such a great composition!")
    comment498 = Comment(user_id=2, image_id=53, comment="This gives me life!")
    comment499 = Comment(user_id=1, image_id=11, comment="Fantastic!")
    comment500 = Comment(user_id=5, image_id=29, comment="So much talent!")
    comment501 = Comment(user_id=7, image_id=8, comment="Incredible work!")
    comment502 = Comment(user_id=3, image_id=25, comment="This is perfection!")
    comment503 = Comment(user_id=6, image_id=16, comment="Absolutely love it!")
    comment504 = Comment(user_id=4, image_id=46, comment="Such an inspiration!")
    comment505 = Comment(user_id=2, image_id=54, comment="I can't stop staring at this!")
    comment506 = Comment(user_id=1, image_id=40, comment="Beautifully captured!")
    comment507 = Comment(user_id=5, image_id=12, comment="What a view!")
    comment508 = Comment(user_id=7, image_id=41, comment="Truly inspiring!")
    comment509 = Comment(user_id=3, image_id=14, comment="This is incredible!")
    comment510 = Comment(user_id=6, image_id=27, comment="Love this perspective!")
    comment511 = Comment(user_id=4, image_id=35, comment="So vivid and alive!")
    comment512 = Comment(user_id=2, image_id=10, comment="Such a stunning image!")
    comment513 = Comment(user_id=1, image_id=49, comment="Fantastic work!")
    comment514 = Comment(user_id=5, image_id=36, comment="Amazing!")
    comment515 = Comment(user_id=7, image_id=24, comment="Wow, just wow!")
    comment516 = Comment(user_id=3, image_id=38, comment="A true gem!")
    comment517 = Comment(user_id=6, image_id=19, comment="Incredible detail!")
    comment518 = Comment(user_id=4, image_id=32, comment="What a stunning shot!")
    comment519 = Comment(user_id=2, image_id=47, comment="This is so unique!")
    comment520 = Comment(user_id=1, image_id=55, comment="Absolutely stunning!")
    comment521 = Comment(user_id=5, image_id=6, comment="So beautiful!")
    comment522 = Comment(user_id=7, image_id=44, comment="I love this piece!")
    comment523 = Comment(user_id=3, image_id=13, comment="Truly captivating!")
    comment524 = Comment(user_id=6, image_id=21, comment="What a beautiful image!")
    comment525 = Comment(user_id=4, image_id=15, comment="Such an inspiring work!")
    comment526 = Comment(user_id=2, image_id=5, comment="Fantastic shot!")
    comment527 = Comment(user_id=1, image_id=31, comment="This is phenomenal!")
    comment528 = Comment(user_id=5, image_id=28, comment="Amazing colors!")
    comment529 = Comment(user_id=7, image_id=3, comment="This is breathtaking!")
    comment530 = Comment(user_id=3, image_id=4, comment="So mesmerizing!")
    comment531 = Comment(user_id=6, image_id=7, comment="Incredible capture!")
    comment532 = Comment(user_id=4, image_id=2, comment="Beautifully done!")
    comment533 = Comment(user_id=2, image_id=30, comment="What a sight!")
    comment534 = Comment(user_id=1, image_id=17, comment="This is so inspiring!")
    comment535 = Comment(user_id=5, image_id=26, comment="I love this style!")
    comment536 = Comment(user_id=7, image_id=8, comment="Amazing composition!")
    comment537 = Comment(user_id=3, image_id=41, comment="Such an impressive shot!")
    comment538 = Comment(user_id=6, image_id=12, comment="Beautiful imagery!")
    comment539 = Comment(user_id=4, image_id=11, comment="So much emotion!")
    comment540 = Comment(user_id=2, image_id=39, comment="This is truly art!")
    comment541 = Comment(user_id=1, image_id=24, comment="What a unique perspective!")
    comment542 = Comment(user_id=5, image_id=10, comment="This is incredible!")
    comment543 = Comment(user_id=7, image_id=18, comment="Such beauty!")
    comment544 = Comment(user_id=3, image_id=23, comment="I am in love with this!")
    comment545 = Comment(user_id=6, image_id=20, comment="Wow, just wow!")
    comment546 = Comment(user_id=4, image_id=42, comment="Such a wonderful piece!")
    comment547 = Comment(user_id=2, image_id=54, comment="Incredible work!")
    comment548 = Comment(user_id=1, image_id=45, comment="This brings me joy!")
    comment549 = Comment(user_id=5, image_id=37, comment="So striking!")
    comment550 = Comment(user_id=7, image_id=29, comment="What an amazing view!")
    comment551 = Comment(user_id=3, image_id=38, comment="So vivid!")
    comment552 = Comment(user_id=6, image_id=22, comment="This is mesmerizing!")
    comment553 = Comment(user_id=4, image_id=8, comment="Beautifully captured!")
    comment554 = Comment(user_id=2, image_id=19, comment="This is spectacular!")
    comment555 = Comment(user_id=1, image_id=50, comment="A true masterpiece!")
    comment556 = Comment(user_id=5, image_id=32, comment="Amazing perspective!")
    comment557 = Comment(user_id=7, image_id=14, comment="Such creativity!")
    comment558 = Comment(user_id=3, image_id=36, comment="This is gorgeous!")
    comment559 = Comment(user_id=6, image_id=27, comment="What a fantastic shot!")
    comment560 = Comment(user_id=4, image_id=16, comment="Absolutely beautiful!")



    lst = [
        on,
        tw,
        th,
        fo,
        fi,
        si,
        se,
        ei,
        ni,
        te,
        comment1,
        comment2,
        comment3,
        comment4,
        comment5,
        comment6,
        comment7,
        comment8,
        comment9,
        comment10,
        comment11,
        comment12,
        comment13,
        comment14,
        comment15,
        comment16,
        comment17,
        comment18,
        comment19,
        comment20,
        comment21,
        comment22,
        comment23,
        comment24,
        comment25,
        comment26,
        comment27,
        comment28,
        comment29,
        comment30,
        comment31,
        comment32,
        comment33,
        comment34,
        comment35,
        comment36,
        comment37,
        comment38,
        comment39,
        comment40,
        comment41,
        comment42,
        comment43,
        comment44,
        comment45,
        comment46,
        comment47,
        comment48,
        comment49,
        comment50,
        comment51,
        comment52,
        comment53,
        comment54,
        comment55,
        comment56,
        comment57,
        comment58,
        comment59,
        comment60,
        comment61,
        comment62,
        comment63,
        comment64,
        comment65,
        comment66,
        comment67,
        comment68,
        comment69,
        comment70,
        comment71,
        comment72,
        comment73,
        comment74,
        comment75,
        comment76,
        comment77,
        comment78,
        comment79,
        comment80,
        comment81,
        comment82,
        comment83,
        comment84,
        comment85,
        comment86,
        comment87,
        comment88,
        comment89,
        comment90,
        comment91,
        comment92,
        comment93,
        comment94,
        comment95,
        comment96,
        comment97,
        comment98,
        comment99,
        comment100,
        comment101,
        comment102,
        comment103,
        comment104,
        comment105,
        comment106,
        comment107,
        comment108,
        comment109,
        comment110,
        comment111,
        comment112,
        comment113,
        comment114,
        comment115,
        comment116,
        comment117,
        comment118,
        comment119,
        comment120,
        comment121,
        comment122,
        comment123,
        comment124,
        comment125,
        comment126,
        comment127,
        comment128,
        comment129,
        comment130,
        comment131,
        comment132,
        comment133,
        comment134,
        comment135,
        comment136,
        comment137,
        comment138,
        comment139,
        comment140,
        comment141,
        comment142,
        comment143,
        comment144,
        comment145,
        comment146,
        comment147,
        comment148,
        comment149,
        comment150,
        comment151,
        comment152,
        comment153,
        comment154,
        comment155,
        comment156,
        comment157,
        comment158,
        comment159,
        comment160,
        comment161,
        comment162,
        comment163,
        comment164,
        comment165,
        comment166,
        comment167,
        comment168,
        comment169,
        comment170,
        comment171,
        comment172,
        comment173,
        comment174,
        comment175,
        comment176,
        comment177,
        comment178,
        comment179,
        comment180,
        comment181,
        comment182,
        comment183,
        comment184,
        comment185,
        comment186,
        comment187,
        comment188,
        comment189,
        comment190,
        comment191,
        comment192,
        comment193,
        comment194,
        comment195,
        comment196,
        comment197,
        comment198,
        comment199,
        comment200,
        comment201,
        comment202,
        comment203,
        comment204,
        comment205,
        comment206,
        comment207,
        comment208,
        comment209,
        comment210,
        comment211,
        comment212,
        comment213,
        comment214,
        comment215,
        comment216,
        comment217,
        comment218,
        comment219,
        comment220,
        comment221,
        comment222,
        comment223,
        comment224,
        comment225,
        comment226,
        comment227,
        comment228,
        comment229,
        comment230,
        comment231,
        comment232,
        comment233,
        comment234,
        comment235,
        comment236,
        comment237,
        comment238,
        comment239,
        comment240,
        comment241,
        comment242,
        comment243,
        comment244,
        comment245,
        comment246,
        comment247,
        comment248,
        comment249,
        comment250,
        comment251,
        comment252,
        comment253,
        comment254,
        comment255,
        comment256,
        comment257,
        comment258,
        comment259,
        comment260,
        comment261,
        comment262,
        comment263,
        comment264,
        comment265,
        comment266,
        comment267,
        comment268,
        comment269,
        comment270,
        comment271,
        comment272,
        comment273,
        comment274,
        comment275,
        comment276,
        comment277,
        comment278,
        comment279,
        comment280,
        comment281,
        comment282,
        comment283,
        comment284,
        comment285,
        comment286,
        comment287,
        comment288,
        comment289,
        comment290,
        comment291,
        comment292,
        comment293,
        comment294,
        comment295,
        comment296,
        comment297,
        comment298,
        comment299,
        comment300,
        comment301,
        comment302,
        comment303,
        comment304,
        comment305,
        comment306,
        comment307,
        comment308,
        comment309,
        comment310,
        comment311,
        comment312,
        comment313,
        comment314,
        comment315,
        comment316,
        comment317,
        comment318,
        comment319,
        comment320,
        comment321,
        comment322,
        comment323,
        comment324,
        comment325,
        comment326,
        comment327,
        comment328,
        comment329,
        comment330,
        comment331,
        comment332,
        comment333,
        comment334,
        comment335,
        comment336,
        comment337,
        comment338,
        comment339,
        comment340,
        comment341,
        comment342,
        comment343,
        comment344,
        comment345,
        comment346,
        comment347,
        comment348,
        comment349,
        comment350,
        comment351,
        comment352,
        comment353,
        comment354,
        comment355,
        comment356,
        comment357,
        comment358,
        comment359,
        comment360,
        comment361,
        comment362,
        comment363,
        comment364,
        comment365,
        comment366,
        comment367,
        comment368,
        comment369,
        comment370,
        comment371,
        comment372,
        comment373,
        comment374,
        comment375,
        comment376,
        comment377,
        comment378,
        comment379,
        comment380,
        comment381,
        comment382,
        comment383,
        comment384,
        comment385,
        comment386,
        comment387,
        comment388,
        comment389,
        comment390,
        comment391,
        comment392,
        comment393,
        comment394,
        comment395,
        comment396,
        comment397,
        comment398,
        comment399,
        comment400,
        comment401,
        comment402,
        comment403,
        comment404,
        comment405,
        comment406,
        comment407,
        comment408,
        comment409,
        comment410,
        comment411,
        comment412,
        comment413,
        comment414,
        comment415,
        comment416,
        comment417,
        comment418,
        comment419,
        comment420,
        comment421,
        comment422,
        comment423,
        comment424,
        comment425,
        comment426,
        comment427,
        comment428,
        comment429,
        comment430,
        comment431,
        comment432,
        comment433,
        comment434,
        comment435,
        comment436,
        comment437,
        comment438,
        comment439,
        comment440,
        comment441,
        comment442,
        comment443,
        comment444,
        comment445,
        comment446,
        comment447,
        comment448,
        comment449,
        comment450,
        comment451,
        comment452,
        comment453,
        comment454,
        comment455,
        comment456,
        comment457,
        comment458,
        comment459,
        comment460,
        comment461,
        comment462,
        comment463,
        comment464,
        comment465,
        comment466,
        comment467,
        comment468,
        comment469,
        comment470,
        comment471,
        comment472,
        comment473,
        comment474,
        comment475,
        comment476,
        comment477,
        comment478,
        comment479,
        comment480,
        comment481,
        comment482,
        comment483,
        comment484,
        comment485,
        comment486,
        comment487,
        comment488,
        comment489,
        comment490,
        comment491,
        comment492,
        comment493,
        comment494,
        comment495,
        comment496,
        comment497,
        comment498,
        comment499,
        comment500,
        comment501,
        comment502,
        comment503,
        comment504,
        comment505,
        comment506,
        comment507,
        comment508,
        comment509,
        comment510,
        comment511,
        comment512,
        comment513,
        comment514,
        comment515,
        comment516,
        comment517,
        comment518,
        comment519,
        comment520,
        comment521,
        comment522,
        comment523,
        comment524,
        comment525,
        comment526,
        comment527,
        comment528,
        comment529,
        comment530,
        comment531,
        comment532,
        comment533,
        comment534,
        comment535,
        comment536,
        comment537,
        comment538,
        comment539,
        comment540,
        comment541,
        comment542,
        comment543,
        comment544,
        comment545,
        comment546,
        comment547,
        comment548,
        comment549,
        comment550,
        comment551,
        comment552,
        comment553,
        comment554,
        comment555,
        comment556,
        comment557,
        comment558,
        comment559,
        comment560,
    ]

    for com in lst:
        db.session.add(com)
    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE"
        )
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()

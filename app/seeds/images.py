from app.models import db, Image, environment, SCHEMA
from sqlalchemy.sql import text

def seed_images():
    on = Image(
        user_id=1,
        url="https://upload.wikimedia.org/wikipedia/commons/d/d9/Opening_chess_position_from_black_side.jpg",
        title="Black Side"
    )
    tw = Image(
        user_id=1,
        url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Chess_piece_-_Black_king.JPG",
        title="Black King"
    )
    th = Image(
        user_id=1,
        url="https://wallpapercave.com/wp/wp5498884.png",
        title="Reincarnated as a Slime",
        description="This is NOT a good anime!",
    )
    fo = Image(
        user_id=2,
        url="https://assets.epicurious.com/photos/58d3fed8e2c8295cfbf4a52f/master/pass/ginger_root_pile_23032017.jpg",
        title="How to cook with Ginger",
        description="I know a few good recipes for ginger, please reach out to me if you want to get started!!!"
    )
    fi = Image(
        user_id=2,
        url="https://cdn.shopify.com/s/files/1/0940/8252/files/Ginger_Root-01_1024x1024.jpg?v=1538426708",
        title="Ginger",
        description="Nuff Said"
    )
    si = Image(
        user_id=2, 
        url="https://a-z-animals.com/media/2022/10/iStock-1253070568.jpg",
        title="New Batch"
    )
    se = Image(
        user_id=2, 
        url="https://www.oxygen.ie/wp-content/uploads/2018/05/ginger.jpg",
        title="Beautiful Ginger King",
        description="We are ginger and we are proud!"
    )
    ei = Image(
        user_id=2,
        url="http://topgingers.weebly.com/uploads/1/9/7/7/19776369/8794572.jpeg",
        title="Ron Weasly"
    )
    ni = Image(
        user_id=3,
        url="https://www.goodcore.co.uk/blog/wp-content/uploads/2019/08/coding-vs-programming-2.jpg",
        title="Ill Never Find a Job"
    )
    te = Image(
        user_id=3,
        url="https://cdn.static-economist.com/sites/default/files/images/2015/09/blogs/economist-explains/code2.png",
        title="Tracking Tweets"
    )
    el = Image(
        user_id=3,
        url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/2d78d141-1f64-44c8-976b-7321284e5147/dfjfdbh-02721342-e03d-4748-965f-f5fd5773baba.png",
        title="Literally so me..."
    )
    i0 = Image(
       user_id=7,
       url="https://picsum.photos/id/102/4320/3240",
       title="Ben Moore photo"
    )
    i1 = Image(
       user_id=5,
       url="https://picsum.photos/id/103/2592/1936",
       title="Ilham Rahmansyah photo"
    )
    i2 = Image(
       user_id=1,
       url="https://picsum.photos/id/104/3840/2160",
       title="Dyaa Eldin photo"
    )
    i3 = Image(
       user_id=3,
       url="https://picsum.photos/id/106/2592/1728",
       title="Arvee Marie photo"
    )
    i4 = Image(
       user_id=7,
       url="https://picsum.photos/id/107/5000/3333",
       title="Lukas Schweizer photo"
    )
    i5 = Image(
       user_id=1,
       url="https://picsum.photos/id/108/2000/1333",
       title="Florian Klauer photo"
    )
    i6 = Image(
       user_id=1,
       url="https://picsum.photos/id/109/4287/2392",
       title="Zwaddi photo"
    )
    i7 = Image(
       user_id=7,
       url="https://picsum.photos/id/110/5000/3333",
       title="Kenneth Thewissen photo"
    )
    i8 = Image(
       user_id=4,
       url="https://picsum.photos/id/111/4400/2656",
       title="Gabe Rodriguez photo"
    )
    i9 = Image(
       user_id=2,
       url="https://picsum.photos/id/112/4200/2800",
       title="Zugr photo"
    )
    i10 = Image(
       user_id=5,
       url="https://picsum.photos/id/113/4168/2464",
       title="Zugr photo"
    )
    i11 = Image(
       user_id=3,
       url="https://picsum.photos/id/114/3264/2448",
       title="Brian Gonzalez photo"
    )
    i12 = Image(
       user_id=4,
       url="https://picsum.photos/id/115/1500/1000",
       title="Christian Hebell photo"
    )
    i13 = Image(
       user_id=2,
       url="https://picsum.photos/id/116/3504/2336",
       title="Anton Sulsky photo"
    )
    i14 = Image(
       user_id=7,
       url="https://picsum.photos/id/117/1544/1024",
       title="Daniel Ebersole photo"
    )
    i15 = Image(
       user_id=1,
       url="https://picsum.photos/id/118/1500/1000",
       title="Rick Waalders photo"
    )
    i16 = Image(
       user_id=1,
       url="https://picsum.photos/id/119/3264/2176",
       title="Nadir Balcikli photo"
    )
    i17 = Image(
       user_id=5,
       url="https://picsum.photos/id/120/4928/3264",
       title="Guillaume photo"
    )
    i18 = Image(
       user_id=1,
       url="https://picsum.photos/id/121/1600/1067",
       title="Radio Pink photo"
    )
    i19 = Image(
       user_id=1,
       url="https://picsum.photos/id/122/4147/2756",
       title="Vadim Sherbakov photo"
    )
    i20 = Image(
       user_id=5,
       url="https://picsum.photos/id/123/4928/3264",
       title="Mark Doda photo"
    )
    i21 = Image(
       user_id=1,
       url="https://picsum.photos/id/124/3504/2336",
       title="Anton Sulsky photo"
    )
    i22 = Image(
       user_id=3,
       url="https://picsum.photos/id/125/1500/1000",
       title="Rick Waalders photo"
    )
    i23 = Image(
       user_id=3,
       url="https://picsum.photos/id/126/4272/2511",
       title="Zugr photo"
    )
    i24 = Image(
       user_id=7,
       url="https://picsum.photos/id/127/4032/2272",
       title="Marcin Czerwinski photo"
    )
    i25 = Image(
       user_id=4,
       url="https://picsum.photos/id/128/3823/2549",
       title="Matteo Minelli photo"
    )
    i26 = Image(
       user_id=5,
       url="https://picsum.photos/id/129/4910/3252",
       title="Charlie Foster photo"
    )
    i27 = Image(
       user_id=6,
       url="https://picsum.photos/id/130/3807/2538",
       title="Ryan Jacques photo"
    )
    i28 = Image(
       user_id=2,
       url="https://picsum.photos/id/131/4698/3166",
       title="Charlie Foster photo"
    )
    i29 = Image(
       user_id=2,
       url="https://picsum.photos/id/132/1600/1066",
       title="Peter Besser photo"
    )
    i30 = Image(
       user_id=4,
       url="https://picsum.photos/id/133/2742/1828",
       title="Dietmar Becker photo"
    )
    i31 = Image(
       user_id=5,
       url="https://picsum.photos/id/134/4928/3264",
       title="Charlie Foster photo"
    )
    i32 = Image(
       user_id=4,
       url="https://picsum.photos/id/135/2560/1920",
       title="Yuriy Khimanin photo"
    )
    i33 = Image(
       user_id=6,
       url="https://picsum.photos/id/136/4032/2272",
       title="Marcin Czerwinski photo"
    )
    i34 = Image(
       user_id=4,
       url="https://picsum.photos/id/137/4752/3168",
       title="Vladimir Kramer photo"
    )
    i35 = Image(
       user_id=5,
       url="https://picsum.photos/id/139/3465/3008",
       title="Steve Richey photo"
    )
    i36 = Image(
       user_id=1,
       url="https://picsum.photos/id/140/2448/2448",
       title="Kundan Ramisetti photo"
    )
    i37 = Image(
       user_id=1,
       url="https://picsum.photos/id/141/2048/1365",
       title="Greg Shield photo"
    )
    i38 = Image(
       user_id=7,
       url="https://picsum.photos/id/142/4272/2848",
       title="Vadim Sherbakov photo"
    )
    i39 = Image(
       user_id=1,
       url="https://picsum.photos/id/143/3600/2385",
       title="Steve Richey photo"
    )
    i40 = Image(
       user_id=2,
       url="https://picsum.photos/id/144/4912/2760",
       title="Mouly Kumar photo"
    )
    i41 = Image(
       user_id=4,
       url="https://picsum.photos/id/145/4288/2848",
       title="Lucas Boesche photo"
    )
    i42 = Image(
       user_id=7,
       url="https://picsum.photos/id/146/5000/3333",
       title="Florian Klauer photo"
    )
    i43 = Image(
       user_id=5,
       url="https://picsum.photos/id/147/2448/2448",
       title="Kundan Ramisetti photo"
    )
    i44 = Image(
       user_id=1,
       url="https://picsum.photos/id/149/3454/2288",
       title="Guillaume photo"
    )
    i45 = Image(
       user_id=3,
       url="https://picsum.photos/id/151/4288/3216",
       title="Edoardo Loru photo"
    )
    i46 = Image(
       user_id=5,
       url="https://picsum.photos/id/152/3888/2592",
       title="Steven Spassov photo"
    )
    i47 = Image(
       user_id=4,
       url="https://picsum.photos/id/153/4763/3155",
       title="Charlie Foster photo"
    )
    i48 = Image(
       user_id=3,
       url="https://picsum.photos/id/154/3264/2176",
       title="Christopher Sardegna photo"
    )
    i49 = Image(
       user_id=6,
       url="https://picsum.photos/id/155/3264/2176",
       title="Christopher Sardegna photo"
    )
    i50 = Image(
       user_id=4,
       url="https://picsum.photos/id/156/2177/3264",
       title="Christopher Sardegna photo"
    )
    i51 = Image(
       user_id=4,
       url="https://picsum.photos/id/157/5000/3914",
       title="koichi nakajima photo"
    )
    i52 = Image(
       user_id=3,
       url="https://picsum.photos/id/158/4836/3224",
       title="Daniel Robert photo"
    )
    i53 = Image(
       user_id=2,
       url="https://picsum.photos/id/159/5000/2460",
       title="Shyamanta Baruah photo"
    )
    i54 = Image(
       user_id=2,
       url="https://picsum.photos/id/160/3200/2119",
       title="Thom photo"
    )
    i55 = Image(
       user_id=1,
       url="https://picsum.photos/id/161/4240/2832",
       title="Chloe Benko-Prieur photo"
    )
    i56 = Image(
       user_id=4,
       url="https://picsum.photos/id/162/1500/998",
       title="Dillon McIntosh photo"
    )
    i57 = Image(
       user_id=3,
       url="https://picsum.photos/id/163/2000/1333",
       title="Linh Nguyen photo"
    )
    i58 = Image(
       user_id=6,
       url="https://picsum.photos/id/164/1200/800",
       title="Linh Nguyen photo"
    )
    i59 = Image(
       user_id=4,
       url="https://picsum.photos/id/165/2000/1333",
       title="Linh Nguyen photo"
    )
    i60 = Image(
       user_id=2,
       url="https://picsum.photos/id/166/1280/720",
       title="Romain Briaux photo"
    )
    i61 = Image(
       user_id=3,
       url="https://picsum.photos/id/167/2896/1944",
       title="petradr photo"
    )
    i62 = Image(
       user_id=7,
       url="https://picsum.photos/id/168/1920/1280",
       title="Joeri Römer photo"
    )
    i63 = Image(
       user_id=3,
       url="https://picsum.photos/id/169/2500/1662",
       title="Noel Lopez photo"
    )
    i64 = Image(
       user_id=4,
       url="https://picsum.photos/id/170/2500/1667",
       title="Noel Lopez photo"
    )
    i65 = Image(
       user_id=2,
       url="https://picsum.photos/id/171/2048/1536",
       title="Riley Briggs photo"
    )
    i66 = Image(
       user_id=6,
       url="https://picsum.photos/id/172/2000/1325",
       title="Aleksi Tappura photo"
    )
    i67 = Image(
       user_id=7,
       url="https://picsum.photos/id/173/1200/737",
       title="Linh Nguyen photo"
    )
    i68 = Image(
       user_id=6,
       url="https://picsum.photos/id/174/1600/589",
       title="Linh Nguyen photo"
    )
    i69 = Image(
       user_id=1,
       url="https://picsum.photos/id/175/2896/1944",
       title="petradr photo"
    )
    i70 = Image(
       user_id=2,
       url="https://picsum.photos/id/176/2500/1662",
       title="Good Free Photos photo"
    )
    i71 = Image(
       user_id=6,
       url="https://picsum.photos/id/177/2515/1830",
       title="Danka & Peter photo"
    )
    i72 = Image(
       user_id=5,
       url="https://picsum.photos/id/178/2592/1936",
       title="Thanun Buranapong photo"
    )
    i73 = Image(
       user_id=2,
       url="https://picsum.photos/id/179/2048/1365",
       title="Angelina Odemchuk photo"
    )
    i74 = Image(
       user_id=2,
       url="https://picsum.photos/id/180/2400/1600",
       title="Galymzhan Abdugalimov photo"
    )
    i75 = Image(
       user_id=5,
       url="https://picsum.photos/id/181/1920/1189",
       title="Nick Turner photo"
    )
    i76 = Image(
       user_id=6,
       url="https://picsum.photos/id/182/2896/1944",
       title="Andrea Boldizsar photo"
    )
    i77 = Image(
       user_id=1,
       url="https://picsum.photos/id/183/2316/1544",
       title="müllermarc photo"
    )
    i78 = Image(
       user_id=3,
       url="https://picsum.photos/id/184/4288/2848",
       title="Tim de Groot photo"
    )
    i79 = Image(
       user_id=2,
       url="https://picsum.photos/id/185/3995/2662",
       title="Tim de Groot photo"
    )
    i80 = Image(
       user_id=2,
       url="https://picsum.photos/id/186/2048/1275",
       title="Simon Pape photo"
    )
    i81 = Image(
       user_id=7,
       url="https://picsum.photos/id/187/4000/2667",
       title="Andre Koch photo"
    )
    i82 = Image(
       user_id=7,
       url="https://picsum.photos/id/188/2896/1936",
       title="Wojtek Witkowski photo"
    )
    i83 = Image(
       user_id=1,
       url="https://picsum.photos/id/189/2048/1536",
       title="Buzo Jesús photo"
    )
    i84 = Image(
       user_id=6,
       url="https://picsum.photos/id/190/2048/1365",
       title="James Forbes photo"
    )
    i85 = Image(
       user_id=4,
       url="https://picsum.photos/id/191/2560/1707",
       title="Alex Talmon photo"
    )
    i86 = Image(
       user_id=5,
       url="https://picsum.photos/id/192/2352/2352",
       title="Adam Przewoski photo"
    )
    i87 = Image(
       user_id=7,
       url="https://picsum.photos/id/193/3578/2451",
       title="Vadim Sherbakov photo"
    )
    i88 = Image(
       user_id=7,
       url="https://picsum.photos/id/194/2000/1325",
       title="Aleksi Tappura photo"
    )
    i89 = Image(
       user_id=7,
       url="https://picsum.photos/id/195/768/1024",
       title="Matthew Skinner photo"
    )
    i90 = Image(
       user_id=4,
       url="https://picsum.photos/id/196/2048/1536",
       title="Dyaa Eldin Moustafa photo"
    )
    i91 = Image(
       user_id=2,
       url="https://picsum.photos/id/197/4272/2848",
       title="Kholodnitskiy Maksim photo"
    )
    i92 = Image(
       user_id=1,
       url="https://picsum.photos/id/198/3456/2304",
       title="Sylwia Bartyzel photo"
    )
    i93 = Image(
       user_id=2,
       url="https://picsum.photos/id/199/2592/1728",
       title="Beto Galetto photo"
    )
    i94 = Image(
       user_id=5,
       url="https://picsum.photos/id/200/1920/1280",
       title="Elias Carlsson photo"
    )
    i95 = Image(
       user_id=6,
       url="https://picsum.photos/id/201/5000/3333",
       title="Craig Garner photo"
    )
    i96 = Image(
       user_id=6,
       url="https://picsum.photos/id/202/2392/1260",
       title="Glen Carrie photo"
    )
    i97 = Image(
       user_id=1,
       url="https://picsum.photos/id/203/4032/3024",
       title="Diogo Tavares photo"
    )
    i98 = Image(
       user_id=2,
       url="https://picsum.photos/id/204/5000/3333",
       title="Tiago Gerken photo"
    )
    i99 = Image(
       user_id=1,
       url="https://picsum.photos/id/206/2880/1800",
       title="Philipp Reiner photo"
    )


    lst = [on, tw, th, fo, fi, si, se, ei, ni, te, el, i0, i1, i2, i3, i4, i5, i6, i7, i8, i9, 
           i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25, i26, 
           i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39, i40, i41, i42, i43, 
           i44, i45, i46, i47, i48, i49, i50, i51, i52, i53, i54, i55, i56, i57, i58, i59, i60, 
           i61, i62, i63, i64, i65, i66, i67, i68, i69, i70, i71, i72, i73, i74, i75, i76, i77, 
           i78, i79, i80, i81, i82, i83, i84, i85, i86, i87, i88, i89, i90, i91, i92, i93, i94, 
           i95, i96, i97, i98, i99]
    for image in lst:
        db.session.add(image)

    db.session.commit()

def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))
        
    db.session.commit()
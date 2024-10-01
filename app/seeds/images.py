from app.models import db, Image, environment, SCHEMA
from sqlalchemy.sql import text


def seed_images():
    on = Image(
        user_id=1,
        url="https://upload.wikimedia.org/wikipedia/commons/d/d9/Opening_chess_position_from_black_side.jpg",
        title="Black Side",
    )
    tw = Image(
        user_id=1,
        url="https://upload.wikimedia.org/wikipedia/commons/f/f1/Chess_piece_-_Black_king.JPG",
        title="Black King",
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
        description="I know a few good recipes for ginger, please reach out to me if you want to get started!!!",
    )
    fi = Image(
        user_id=2,
        url="https://cdn.shopify.com/s/files/1/0940/8252/files/Ginger_Root-01_1024x1024.jpg?v=1538426708",
        title="Ginger",
        description="Nuff Said",
    )
    si = Image(
        user_id=2,
        url="https://a-z-animals.com/media/2022/10/iStock-1253070568.jpg",
        title="New Batch",
    )
    se = Image(
        user_id=2,
        url="https://www.oxygen.ie/wp-content/uploads/2018/05/ginger.jpg",
        title="Beautiful Ginger King",
        description="We are ginger and we are proud!",
    )
    ei = Image(
        user_id=2,
        url="http://topgingers.weebly.com/uploads/1/9/7/7/19776369/8794572.jpeg",
        title="Ron Weasly",
    )
    ni = Image(
        user_id=3,
        url="https://www.goodcore.co.uk/blog/wp-content/uploads/2019/08/coding-vs-programming-2.jpg",
        title="Ill Never Find a Job",
    )
    te = Image(
        user_id=3,
        url="https://cdn.static-economist.com/sites/default/files/images/2015/09/blogs/economist-explains/code2.png",
        title="Tracking Tweets",
    )
    el = Image(
        user_id=3,
        url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/2d78d141-1f64-44c8-976b-7321284e5147/dfjfdbh-02721342-e03d-4748-965f-f5fd5773baba.png",
        title="Literally so me...",
    )
    i0 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_0.jpg",
        title="Ben Moore photo",
    )
    i1 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_1.jpg",
        title="Ilham Rahmansyah photo",
    )
    i2 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_2.jpg",
        title="Dyaa Eldin photo",
    )
    i3 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_3.jpg",
        title="Arvee Marie photo",
    )
    i4 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_4.jpg",
        title="Lukas Schweizer photo",
    )
    i5 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_5.jpg",
        title="Florian Klauer photo",
    )
    i6 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_6.jpg",
        title="Zwaddi photo",
    )
    i7 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_7.jpg",
        title="Kenneth Thewissen photo",
    )
    i8 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_8.jpg",
        title="Gabe Rodriguez photo",
    )
    i9 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_9.jpg",
        title="Zugr photo",
    )
    i10 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_10.jpg",
        title="Zugr photo",
    )
    i11 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_11.jpg",
        title="Brian Gonzalez photo",
    )
    i12 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_12.jpg",
        title="Christian Hebell photo",
    )
    i13 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_13.jpg",
        title="Anton Sulsky photo",
    )
    i14 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_14.jpg",
        title="Daniel Ebersole photo",
    )
    i15 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_15.jpg",
        title="Rick Waalders photo",
    )
    i16 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_16.jpg",
        title="Nadir Balcikli photo",
    )
    i17 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_17.jpg",
        title="Guillaume photo",
    )
    i18 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_18.jpg",
        title="Radio Pink photo",
    )
    i19 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_19.jpg",
        title="Vadim Sherbakov photo",
    )
    i20 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_20.jpg",
        title="Mark Doda photo",
    )
    i21 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_21.jpg",
        title="Anton Sulsky photo",
    )
    i22 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_22.jpg",
        title="Rick Waalders photo",
    )
    i23 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_23.jpg",
        title="Zugr photo",
    )
    i24 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_24.jpg",
        title="Marcin Czerwinski photo",
    )
    i25 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_25.jpg",
        title="Matteo Minelli photo",
    )
    i26 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_26.jpg",
        title="Charlie Foster photo",
    )
    i27 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_27.jpg",
        title="Ryan Jacques photo",
    )
    i28 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_28.jpg",
        title="Charlie Foster photo",
    )
    i29 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_29.jpg",
        title="Peter Besser photo",
    )
    i30 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_30.jpg",
        title="Dietmar Becker photo",
    )
    i31 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_31.jpg",
        title="Charlie Foster photo",
    )
    i32 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_32.jpg",
        title="Yuriy Khimanin photo",
    )
    i33 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_33.jpg",
        title="Marcin Czerwinski photo",
    )
    i34 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_34.jpg",
        title="Vladimir Kramer photo",
    )
    i35 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_35.jpg",
        title="Steve Richey photo",
    )
    i36 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_36.jpg",
        title="Kundan Ramisetti photo",
    )
    i37 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_37.jpg",
        title="Greg Shield photo",
    )
    i38 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_38.jpg",
        title="Vadim Sherbakov photo",
    )
    i39 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_39.jpg",
        title="Steve Richey photo",
    )
    i40 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_40.jpg",
        title="Mouly Kumar photo",
    )
    i41 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_41.jpg",
        title="Lucas Boesche photo",
    )
    i42 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_42.jpg",
        title="Florian Klauer photo",
    )
    i43 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_43.jpg",
        title="Kundan Ramisetti photo",
    )
    i44 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_44.jpg",
        title="Guillaume photo",
    )
    i45 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_45.jpg",
        title="Edoardo Loru photo",
    )
    i46 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_46.jpg",
        title="Steven Spassov photo",
    )
    i47 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_47.jpg",
        title="Charlie Foster photo",
    )
    i48 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_48.jpg",
        title="Christopher Sardegna photo",
    )
    i49 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_49.jpg",
        title="Christopher Sardegna photo",
    )
    i50 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_50.jpg",
        title="Christopher Sardegna photo",
    )
    i51 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_51.jpg",
        title="koichi nakajima photo",
    )
    i52 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_52.jpg",
        title="Daniel Robert photo",
    )
    i53 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_53.jpg",
        title="Shyamanta Baruah photo",
    )
    i54 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_54.jpg",
        title="Thom photo",
    )
    i55 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_55.jpg",
        title="Chloe Benko-Prieur photo",
    )
    i56 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_56.jpg",
        title="Dillon McIntosh photo",
    )
    i57 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_57.jpg",
        title="Linh Nguyen photo",
    )
    i58 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_58.jpg",
        title="Linh Nguyen photo",
    )
    i59 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_59.jpg",
        title="Linh Nguyen photo",
    )
    i60 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_60.jpg",
        title="Romain Briaux photo",
    )
    i61 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_61.jpg",
        title="petradr photo",
    )
    i62 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_62.jpg",
        title="Joeri Römer photo",
    )
    i63 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_63.jpg",
        title="Noel Lopez photo",
    )
    i64 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_64.jpg",
        title="Noel Lopez photo",
    )
    i65 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_65.jpg",
        title="Riley Briggs photo",
    )
    i66 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_66.jpg",
        title="Aleksi Tappura photo",
    )
    i67 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_67.jpg",
        title="Linh Nguyen photo",
    )
    i68 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_68.jpg",
        title="Linh Nguyen photo",
    )
    i69 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_69.jpg",
        title="petradr photo",
    )
    i70 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_70.jpg",
        title="Good Free Photos photo",
    )
    i71 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_71.jpg",
        title="Danka & Peter photo",
    )
    i72 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_72.jpg",
        title="Thanun Buranapong photo",
    )
    i73 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_73.jpg",
        title="Angelina Odemchuk photo",
    )
    i74 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_74.jpg",
        title="Galymzhan Abdugalimov photo",
    )
    i75 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_75.jpg",
        title="Nick Turner photo",
    )
    i76 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_76.jpg",
        title="Andrea Boldizsar photo",
    )
    i77 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_77.jpg",
        title="müllermarc photo",
    )
    i78 = Image(
        user_id=3,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_78.jpg",
        title="Tim de Groot photo",
    )
    i79 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_79.jpg",
        title="Tim de Groot photo",
    )
    i80 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_80.jpg",
        title="Simon Pape photo",
    )
    i81 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_81.jpg",
        title="Andre Koch photo",
    )
    i82 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_82.jpg",
        title="Wojtek Witkowski photo",
    )
    i83 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_83.jpg",
        title="Buzo Jesús photo",
    )
    i84 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_84.jpg",
        title="James Forbes photo",
    )
    i85 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_85.jpg",
        title="Alex Talmon photo",
    )
    i86 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_86.jpg",
        title="Adam Przewoski photo",
    )
    i87 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_87.jpg",
        title="Vadim Sherbakov photo",
    )
    i88 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_88.jpg",
        title="Aleksi Tappura photo",
    )
    i89 = Image(
        user_id=7,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_89.jpg",
        title="Matthew Skinner photo",
    )
    i90 = Image(
        user_id=4,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_90.jpg",
        title="Dyaa Eldin Moustafa photo",
    )
    i91 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_91.jpg",
        title="Kholodnitskiy Maksim photo",
    )
    i92 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_92.jpg",
        title="Sylwia Bartyzel photo",
    )
    i93 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_93.jpg",
        title="Beto Galetto photo",
    )
    i94 = Image(
        user_id=5,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_94.jpg",
        title="Elias Carlsson photo",
    )
    i95 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_95.jpg",
        title="Craig Garner photo",
    )
    i96 = Image(
        user_id=6,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_96.jpg",
        title="Glen Carrie photo",
    )
    i97 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_97.jpg",
        title="Diogo Tavares photo",
    )
    i98 = Image(
        user_id=2,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_98.jpg",
        title="Tiago Gerken photo",
    )
    i99 = Image(
        user_id=1,
        url="https://jds-images-bucket.s3.us-east-2.amazonaws.com/seed_image_99.jpg",
        title="Philipp Reiner photo",
    )

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
        el,
        i0,
        i1,
        i2,
        i3,
        i4,
        i5,
        i6,
        i7,
        i8,
        i9,
        i10,
        i11,
        i12,
        i13,
        i14,
        i15,
        i16,
        i17,
        i18,
        i19,
        i20,
        i21,
        i22,
        i23,
        i24,
        i25,
        i26,
        i27,
        i28,
        i29,
        i30,
        i31,
        i32,
        i33,
        i34,
        i35,
        i36,
        i37,
        i38,
        i39,
        i40,
        i41,
        i42,
        i43,
        i44,
        i45,
        i46,
        i47,
        i48,
        i49,
        i50,
        i51,
        i52,
        i53,
        i54,
        i55,
        i56,
        i57,
        i58,
        i59,
        i60,
        i61,
        i62,
        i63,
        i64,
        i65,
        i66,
        i67,
        i68,
        i69,
        i70,
        i71,
        i72,
        i73,
        i74,
        i75,
        i76,
        i77,
        i78,
        i79,
        i80,
        i81,
        i82,
        i83,
        i84,
        i85,
        i86,
        i87,
        i88,
        i89,
        i90,
        i91,
        i92,
        i93,
        i94,
        i95,
        i96,
        i97,
        i98,
        i99,
    ]
    for image in lst:
        db.session.add(image)

    db.session.commit()


def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))

    db.session.commit()

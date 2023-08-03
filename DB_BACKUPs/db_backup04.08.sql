toc.dat                                                                                             0000600 0004000 0002000 00000023070 14463016231 0014441 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP                            {        	   marketapp    13.11 (Debian 13.11-0+deb11u1)    13.11 (Debian 13.11-0+deb11u1)     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         �           1262    16687 	   marketapp    DATABASE     ^   CREATE DATABASE marketapp WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';
    DROP DATABASE marketapp;
                alex    false         �           0    0    DATABASE marketapp    ACL     S   GRANT ALL ON DATABASE marketapp TO raya;
GRANT ALL ON DATABASE marketapp TO bobby;
                   alex    false    3054         �            1259    33276    basket    TABLE     �   CREATE TABLE public.basket (
    username text NOT NULL,
    product_id text NOT NULL,
    product_name text NOT NULL,
    quantity numeric(10,2) NOT NULL,
    total_value smallint NOT NULL
);
    DROP TABLE public.basket;
       public         heap    raya    false         �            1259    16815 
   categories    TABLE     G  CREATE TABLE public.categories (
    category_id text NOT NULL,
    category_name text NOT NULL,
    total_subcategories integer NOT NULL,
    total_items integer NOT NULL,
    last_modified timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    category_description text,
    category_function text,
    image_url text
);
    DROP TABLE public.categories;
       public         heap    raya    false         �            1259    16693 	   customers    TABLE     ;  CREATE TABLE public.customers (
    customer_id bigint NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email_address text NOT NULL,
    phone text NOT NULL,
    registration_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    username text,
    total_orders integer
);
    DROP TABLE public.customers;
       public         heap    raya    false         �           0    0    TABLE customers    ACL     F   GRANT SELECT,UPDATE ON TABLE public.customers TO customers_marketapp;
          public          raya    false    200         �            1259    16710 	   employees    TABLE     �   CREATE TABLE public.employees (
    employee_id smallint NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email_address character varying(30) NOT NULL,
    phone text NOT NULL
);
    DROP TABLE public.employees;
       public         heap    raya    false         �           0    0    TABLE employees    ACL     F   GRANT SELECT,UPDATE ON TABLE public.employees TO customers_marketapp;
          public          raya    false    201         �            1259    25094    favourite_products    TABLE     �   CREATE TABLE public.favourite_products (
    username character varying(50),
    product_id character varying(10),
    product_name character varying(50)
);
 &   DROP TABLE public.favourite_products;
       public         heap    alex    false         �            1259    33282    orders    TABLE     �  CREATE TABLE public.orders (
    order_id text NOT NULL,
    username text NOT NULL,
    product_id text NOT NULL,
    product_name text NOT NULL,
    single_price numeric(10,2) NOT NULL,
    quantity numeric(10,2) NOT NULL,
    total_value numeric(10,2) GENERATED ALWAYS AS ((single_price * quantity)) STORED,
    date_ordered timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.orders;
       public         heap    raya    false         �            1259    16892    payment_options    TABLE     �   CREATE TABLE public.payment_options (
    payment_code text NOT NULL,
    payment_name text,
    payment_type text,
    card_number text,
    card_holder text,
    ccv numeric,
    expire_date date,
    default_option boolean,
    username text
);
 #   DROP TABLE public.payment_options;
       public         heap    alex    false         �            1259    16849    products    TABLE     �  CREATE TABLE public.products (
    product_id text NOT NULL,
    product_name text NOT NULL,
    category text NOT NULL,
    subcategory text NOT NULL,
    single_price numeric(10,2) NOT NULL,
    quantity numeric(10,2) NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    total_value numeric(10,2) GENERATED ALWAYS AS ((single_price * quantity)) STORED,
    unit_of_measure text,
    product_description character varying
);
    DROP TABLE public.products;
       public         heap    alex    false         �            1259    16832    subcategories    TABLE     �   CREATE TABLE public.subcategories (
    subcategory_id text NOT NULL,
    subcategory_name text NOT NULL,
    total_items integer NOT NULL,
    last_modified timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    parent_category text
);
 !   DROP TABLE public.subcategories;
       public         heap    raya    false         �          0    33276    basket 
   TABLE DATA           [   COPY public.basket (username, product_id, product_name, quantity, total_value) FROM stdin;
    public          raya    false    207       3047.dat �          0    16815 
   categories 
   TABLE DATA           �   COPY public.categories (category_id, category_name, total_subcategories, total_items, last_modified, category_description, category_function, image_url) FROM stdin;
    public          raya    false    202       3042.dat �          0    16693 	   customers 
   TABLE DATA           �   COPY public.customers (customer_id, first_name, last_name, email_address, phone, registration_date, username, total_orders) FROM stdin;
    public          raya    false    200       3040.dat �          0    16710 	   employees 
   TABLE DATA           ]   COPY public.employees (employee_id, first_name, last_name, email_address, phone) FROM stdin;
    public          raya    false    201       3041.dat �          0    25094    favourite_products 
   TABLE DATA           P   COPY public.favourite_products (username, product_id, product_name) FROM stdin;
    public          alex    false    206       3046.dat �          0    33282    orders 
   TABLE DATA           t   COPY public.orders (order_id, username, product_id, product_name, single_price, quantity, date_ordered) FROM stdin;
    public          raya    false    208       3048.dat �          0    16892    payment_options 
   TABLE DATA           �   COPY public.payment_options (payment_code, payment_name, payment_type, card_number, card_holder, ccv, expire_date, default_option, username) FROM stdin;
    public          alex    false    205       3045.dat �          0    16849    products 
   TABLE DATA           �   COPY public.products (product_id, product_name, category, subcategory, single_price, quantity, date_created, unit_of_measure, product_description) FROM stdin;
    public          alex    false    204       3044.dat �          0    16832    subcategories 
   TABLE DATA           v   COPY public.subcategories (subcategory_id, subcategory_name, total_items, last_modified, parent_category) FROM stdin;
    public          raya    false    203       3043.dat W           2606    16823    categories categories_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public            raya    false    202         S           2606    16774 #   customers customers_customer_id_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_customer_id_key UNIQUE (customer_id);
 M   ALTER TABLE ONLY public.customers DROP CONSTRAINT customers_customer_id_key;
       public            raya    false    200         U           2606    16717 #   employees employees_employee_id_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_employee_id_key UNIQUE (employee_id);
 M   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_employee_id_key;
       public            raya    false    201         ]           2606    16899 $   payment_options payment_options_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.payment_options
    ADD CONSTRAINT payment_options_pkey PRIMARY KEY (payment_code);
 N   ALTER TABLE ONLY public.payment_options DROP CONSTRAINT payment_options_pkey;
       public            alex    false    205         [           2606    16857    products products_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            alex    false    204         Y           2606    16840     subcategories subcategories_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.subcategories
    ADD CONSTRAINT subcategories_pkey PRIMARY KEY (subcategory_id);
 J   ALTER TABLE ONLY public.subcategories DROP CONSTRAINT subcategories_pkey;
       public            raya    false    203                                                                                                                                                                                                                                                                                                                                                                                                                                                                                3047.dat                                                                                            0000600 0004000 0002000 00000000005 14463016231 0014242 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           3042.dat                                                                                            0000600 0004000 0002000 00000003212 14463016231 0014240 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        CAT-821620	Accessories	3	13	2023-05-19 12:15:16.17974	All kind of accessories here!	accessories	https://images.app.goo.gl/Qk242WM6hBe56aCQ6
CAT-314816	Cosmetics	3	9	2023-05-19 11:55:21.893555	Cosmetics for everyone!	cosmetics	https://images.app.goo.gl/UWwsxuuG7NKNR4Hv5
CAT-363803	Hair	3	9	2023-05-19 12:24:00.685837	Many healthy things for your hair here!	hair	https://images.app.goo.gl/f5nvEDph1yzURHwb7
CAT-181291	Home and Living	3	9	2023-05-19 11:56:32.928574	Everything for your home!	homeandliving	https://images.app.goo.gl/UkpEkbCuS5oCVEVh9
CAT-360035	Beachwear	6	9	2023-05-19 12:16:45.248848	Anything for the beach you can find is here!	beachwear	https://images.app.goo.gl/UNgzBfepKswJRQwL8
CAT-953732	Drinks	3	9	2023-05-19 11:51:37.197437	Find all drinks here!	drinks	https://images.app.goo.gl/1kr39sC5ryKSFcfB7
CAT-584109	Shoes	3	9	2023-05-19 12:10:57.61498	Every different kind of shoes here!	shoes	https://images.app.goo.gl/ENETVsfDjkC86yVm9
CAT-177703	Electronics	3	9	2023-05-19 12:05:45.844296	Find everything you need for your computer and others!	electronics	https://images.app.goo.gl/3XVce8jEJ2aChiQU8
CAT-872552	Books	3	9	2023-05-19 11:52:52.477528	Read all the books we have!	books	https://images.app.goo.gl/y898YQTGFXn5mCv59
CAT-795326	Clothes	6	9	2023-05-19 11:53:43.813573	Have your new clothes from here!	clothes	https://images.app.goo.gl/WNEcwoMLLNnu6R238
CAT-239320	Food	3	9	2023-05-19 11:50:36.503393	Find whatever you like eating here!	food	https://images.app.goo.gl/4H8yYtfftKY3vFev6
CAT-375354	Sports	3	9	2023-05-19 12:23:23.711324	Find shoes, clothes and many others for your sport here!	sports	https://images.app.goo.gl/CBvbUGM88dswuwto9
\.


                                                                                                                                                                                                                                                                                                                                                                                      3040.dat                                                                                            0000600 0004000 0002000 00000000574 14463016231 0014246 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        8788935163	Pesho	Peshev	pesho@example.com	555-123-555	2023-05-27 14:32:17.00807	pesho	0
5043658785	Nikolay	Georgiev	udiewqad@gmail.com	3821903821	2023-06-19 13:36:47.339687	nikirich	\N
3545241682	hello	hello	jdsioafe@gmail.com	1234567890	2023-07-08 14:03:18.652514	hello	\N
3710119698	Nikolay	Georgieb	jewoifnd@gmail.com	1234567891	2023-07-15 14:40:28.452835	nikicha_test	\N
\.


                                                                                                                                    3041.dat                                                                                            0000600 0004000 0002000 00000000005 14463016231 0014234 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           3046.dat                                                                                            0000600 0004000 0002000 00000000416 14463016231 0014247 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        pesho	SKU-607978	Vegetables1
pesho	SKU-337325	Vegetables2
pesho	SKU-227440	Vegetables3
pesho	SKU-151819	MakeUp1
pesho	SKU-847225	MakeUp2
pesho	SKU-202045	MakeUp3
pesho	SKU-906629	MenShorts2
pesho	SKU-612016	Wallet1
pesho	SKU-269114	Wallet2
pesho	SKU-525292	Wallet3
\.


                                                                                                                                                                                                                                                  3048.dat                                                                                            0000600 0004000 0002000 00000000005 14463016231 0014243 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        \.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           3045.dat                                                                                            0000600 0004000 0002000 00000000247 14463016231 0014250 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PAY-123456	My-Visa	Visa	1234-1234-1234	Pesho Peshev	123	2025-06-11	t	pesho
PAY-112233	My-MasterCard	MasterCard	4321-4321-4321	Pesho Peshev	223	2025-06-11	f	pesho
\.


                                                                                                                                                                                                                                                                                                                                                         3044.dat                                                                                            0000600 0004000 0002000 00000027551 14463016231 0014256 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        SKU-025512	Sunglasses1	Accessories	Sunglasses	45.99	41.00	2023-06-10 21:08:57.871275	pcs	Men Solid Wrap Fashion Glasses For Daily Decoration
SKU-859357	Sunglasses2	Accessories	Sunglasses	34.50	59.00	2023-06-10 21:14:25.476657	pcs	Geometric Frame Black Fashion Glasses
SKU-778002	Sunglasses3	Accessories	Sunglasses	50.99	30.00	2023-06-10 21:15:42.356198	pcs	Women Geometric Frame Boho Fashion Glasses For Outdoor
SKU-708855	Watches2	Accessories	Watches	230.89	46.00	2023-06-10 21:34:01.955891	pcs	Men Black Nylon Strap Casual Round Watch
SKU-323357	Watches3	Accessories	Watches	189.99	58.00	2023-06-10 21:34:59.124787	pcs	Mesh Strap Round Pointer Quartz Watch
SKU-612016	Wallet1	Accessories	Wallets	50.75	34.00	2023-06-10 21:38:43.870206	pcs	Crocodile Embossed Flap Small Wallet
SKU-269114	Wallet2	Accessories	Wallets	78.99	55.00	2023-06-10 21:39:52.112009	pcs	Men Letter Graphic Small Wallet
SKU-525292	Wallet3	Accessories	Wallets	45.89	38.00	2023-06-10 21:40:43.901692	pcs	Letter Graphic Small Pocket Wallet
SKU-269217	Watches1	Accessories	Watches	120.99	37.00	2023-06-10 21:33:01.634615	pcs	Women White PU Polyurethane Strap Elegant Watch
SKU-685589	MenShorts1	Beachwear	Men Shorts	22.99	47.00	2023-06-17 20:49:05.885767	pcs	Men Neon Orange Tropical Shorts
SKU-906629	MenShorts2	Beachwear	Men Shorts	46.89	34.00	2023-06-17 20:52:11.575556	pcs	Random Cartoon Duck Print Shorts
SKU-564056	MenShorts3	Beachwear	Men Shorts	21.00	34.00	2023-06-17 20:54:34.522228	pcs	Solid Drawstring Waist Shorts
SKU-905327	WomenKimono1	Beachwear	Women Kimonos	33.45	45.00	2023-06-17 21:07:10.933414	pcs	Fashion Print Kimono
SKU-776868	WomenKimono2	Beachwear	Women Kimonos	29.99	23.00	2023-06-17 21:07:58.465666	pcs	Patchwork Print Kimono
SKU-275298	WomenKimono3	Beachwear	Women Kimonos	34.50	24.00	2023-06-17 21:09:12.216227	pcs	Casual Loose Kimono
SKU-793659	BeachShoes1	Beachwear	Beach Shoes	14.90	30.00	2023-06-17 21:10:15.970876	pcs	Thick Sole Slippers
SKU-415610	BeachShoes2	Beachwear	Beach Shoes	33.90	34.00	2023-06-17 21:11:03.163326	pcs	Men Graffiti Flip Flops
SKU-175842	BeachShoes3	Beachwear	Beach Shoes	29.80	36.00	2023-06-17 21:12:06.079203	pcs	Letter Graphic Flip Flops
SKU-275108	Horror1	Books	Horror	16.99	15.00	2023-06-17 21:26:39.673336	pcs	Anna Dressed In Blood
SKU-150601	Horror2	Books	Horror	19.80	31.00	2023-06-17 21:28:30.765739	pcs	Miss Peregrines Home For Peculiar Children
SKU-345594	Horror3	Books	Horror	21.90	29.00	2023-06-17 21:29:24.801394	pcs	The Demonata Lord Loss
SKU-282223	Romance1	Books	Romance	21.99	34.00	2023-06-17 21:33:07.466119	pcs	The Love Hypothesis
SKU-105007	Romance2	Books	Romance	23.79	29.00	2023-06-17 21:33:50.672519	pcs	It Ends With Us
SKU-375700	Romance3	Books	Romance	18.29	45.00	2023-06-17 21:34:32.053702	pcs	The Summer Of Broken Rules
SKU-912523	Documentary1	Books	Documentary	23.59	34.00	2023-06-22 22:36:11.522022	pcs	Documenting Syria
SKU-549259	Documentary2	Books	Documentary	33.99	24.00	2023-06-22 22:37:32.600706	pcs	We Keep The Dead Close
SKU-485643	Documentary3	Books	Documentary	21.79	43.00	2023-06-22 22:38:44.009485	pcs	Master Thieves
SKU-018243	Blouses1	Clothes	Blouses	34.59	24.00	2023-06-22 23:02:13.345934	pcs	Mulvari Collared Floral Blouse
SKU-362132	Blouses2	Clothes	Blouses	44.40	36.00	2023-06-22 23:03:16.229021	pcs	Figure Graphic Knot Blouse
SKU-612972	Blouses3	Clothes	Blouses	45.99	38.00	2023-06-22 23:05:35.360732	pcs	Long Sleeve Shirt
SKU-521402	Skirts1	Clothes	Skirts	16.79	36.00	2023-06-22 23:27:14.656048	pcs	Ditsy Floral Skirt
SKU-800115	Skirts2	Clothes	Skirts	34.00	14.00	2023-06-22 23:28:02.247943	pcs	Paisley Print Ruffle Skirt
SKU-548001	Skirts3	Clothes	Skirts	29.99	41.00	2023-06-22 23:28:45.084988	pcs	Solid Pleated Skirt
SKU-923690	Suits1	Clothes	Men Suits	99.80	56.00	2023-06-22 23:34:53.587888	pcs	Manfinity Mode Blue Suit
SKU-985003	Suits2	Clothes	Men Suits	120.40	45.00	2023-06-22 23:35:52.050312	pcs	Manfinity Mode Black Suit
SKU-206532	Suits3	Clothes	Men Suits	114.59	39.00	2023-06-22 23:37:00.657934	pcs	Manfinity Mode Grey Suit
SKU-151819	MakeUp1	Cosmetics	Makeup	44.55	56.00	2023-06-29 21:31:28.708852	pcs	Eyeshadow Palette
SKU-847225	MakeUp2	Cosmetics	Makeup	23.99	41.00	2023-06-29 21:32:50.623227	pcs	Moisturizing Lip Oil Gloss
SKU-202045	MakeUp3	Cosmetics	Makeup	34.60	28.00	2023-06-29 21:33:34.581732	pcs	High Coverage Concealer
SKU-595178	NailPolish1	Cosmetics	Nail Polish	14.50	29.00	2023-06-29 21:41:49.383576	pcs	Lavender Violets Matte Gel Nail Polish
SKU-817593	NailPolish2	Cosmetics	Nail Polish	31.99	53.00	2023-06-29 21:42:35.18231	pcs	French Style Nail Polish
SKU-163583	NailPolish3	Cosmetics	Nail Polish	19.20	43.00	2023-06-29 21:43:33.554442	pcs	Quick-drying Nail Polish Set
SKU-110023	SkinCare1	Cosmetics	Skin Care Products	45.90	30.00	2023-06-29 21:48:57.943308	pcs	Lip Scrub & Lip Mask
SKU-525581	SkinCare2	Cosmetics	Skin Care Products	14.60	34.00	2023-06-29 21:49:57.306193	pcs	Oil-Absorbing Paper
SKU-623343	SkinCare3	Cosmetics	Skin Care Products	21.45	24.00	2023-06-29 21:50:42.996306	pcs	Mite Removal Soap
SKU-086277	AlcoholBeverages1	Drinks	Alcohol Beverages	7.99	80.00	2023-06-29 22:07:44.028691	pcs	Beer Heineken
SKU-728746	AlcoholBeverages2	Drinks	Alcohol Beverages	30.99	40.00	2023-06-29 22:08:42.77457	pcs	Absolut Vodka
SKU-102732	AlcoholBeverages3	Drinks	Alcohol Beverages	56.99	50.00	2023-06-29 22:09:22.020045	pcs	Whiskey Jameson
SKU-339003	Non-Alcohol1	Drinks	Non-Alcohol Beverages	4.60	60.00	2023-06-29 22:16:55.799356	pcs	Rita Sparkling Strawberry Juice
SKU-933828	Non-Alcohol2	Drinks	Non-Alcohol Beverages	9.80	58.00	2023-06-29 22:17:50.508753	pcs	Starbucks Tropical Drink
SKU-075612	Non-Alcohol3	Drinks	Non-Alcohol Beverages	6.80	44.00	2023-06-29 22:18:41.325509	pcs	Virgin Miami Vice
SKU-962481	Coffee1	Drinks	Coffee	4.90	50.00	2023-06-29 22:27:27.940944	pcs	Pumpkin Spice Latte
SKU-687919	Coffee2	Drinks	Coffee	6.99	30.00	2023-06-29 22:28:26.928985	pcs	Latte Coffee
SKU-988563	Coffee3	Drinks	Coffee	7.60	67.00	2023-06-29 22:29:12.334523	pcs	Mocha Coffee
SKU-328920	PhotographyGadgets1	Electronics	Photography Gadgets	134.99	56.00	2023-06-30 22:28:28.792132	pcs	Ultimate Lens Hood
SKU-149227	PhotographyGadgets2	Electronics	Photography Gadgets	98.60	30.00	2023-06-30 22:30:12.707237	pcs	Tourbox Controller
SKU-529169	PhotographyGadgets3	Electronics	Photography Gadgets	23.40	45.00	2023-06-30 22:31:30.668554	pcs	Recycled Camera Focus Lens Cuffs
SKU-150048	Computers1	Electronics	Computers	791.90	80.00	2023-06-30 22:50:09.119507	pcs	DELL Vostro 3910 MT Core I3-12100
SKU-286792	Computers2	Electronics	Computers	2089.99	67.00	2023-06-30 22:52:55.553358	pcs	Acer Nitro N50-640, i5-12400F, 8GB
SKU-372826	Computers3	Electronics	Computers	1929.89	90.00	2023-06-30 22:54:34.700925	pcs	Powered by Asus level Five (Ryzen 5 5500, 8GB)
SKU-123301	HouseholdAppliances1	Electronics	Household Appliances	67.99	50.00	2023-06-30 23:16:39.163226	pcs	Coffee Machine Breville VCF109X Prima Latte II
SKU-615910	HouseholdAppliances2	Electronics	Household Appliances	120.49	45.00	2023-06-30 23:17:51.531674	pcs	Blender Philips - Series 3000
SKU-171568	HouseholdAppliances3	Electronics	Household Appliances	114.50	32.00	2023-06-30 23:18:57.4235	pcs	Electric Bread Toaster
SKU-774384	Fruits1	Food	Fruits	6.70	10.00	2023-07-02 16:47:56.819239	pcs	Bananas
SKU-731101	Fruits2	Food	Fruits	7.80	12.00	2023-07-02 16:48:36.214332	pcs	Golden Pineapples
SKU-667927	Fruits3	Food	Fruits	6.40	11.00	2023-07-02 16:49:17.744322	kg	Succulent Cherries
SKU-920544	Meat1	Food	Meat	15.80	3.00	2023-07-02 16:52:25.91004	pcs	Chicken Wings
SKU-478638	Meat2	Food	Meat	20.30	7.00	2023-07-02 16:53:12.40253	kg	Pork Ribs
SKU-681104	Meat3	Food	Meat	19.99	5.00	2023-07-02 16:54:10.048705	kg	Beef Steak
SKU-607978	Vegetables1	Food	Vegetables	6.70	10.00	2023-07-02 16:57:38.557375	kg	Cucumbers
SKU-337325	Vegetables2	Food	Vegetables	3.40	20.00	2023-07-02 16:58:16.082908	pcs	Green Cabbages
SKU-227440	Vegetables3	Food	Vegetables	4.50	9.00	2023-07-02 16:58:53.826379	kg	Mushrooms
SKU-956046	Accessories1	Hair	Accessories	11.30	15.00	2023-07-02 17:07:18.476836	pcs	Mini Star Shaped Hair Clips
SKU-117550	Accessories2	Hair	Accessories	5.70	20.00	2023-07-02 17:08:19.792466	pcs	Elastic Hair Scrunchies
SKU-454750	Accessories3	Hair	Accessories	2.00	36.00	2023-07-02 17:09:25.888152	pcs	Star Charm Hair Rings
SKU-021518	ElectricalGadgets1	Hair	Electrical Gadgets	110.24	50.00	2023-07-16 16:38:40.256015	pcs	Instyler Max 2-way Rotating Iron
SKU-481599	ElectricalGadgets2	Hair	Electrical Gadgets	230.90	78.00	2023-07-16 16:40:36.118501	pcs	Panasonic Spa-Quality Facial Steamer
SKU-547352	ElectricalGadgets3	Hair	Electrical Gadgets	68.99	67.00	2023-07-16 16:41:56.275502	pcs	Hydro Fusion Anti Frizz Hair Straightener
SKU-401772	Products1	Hair	Products	13.40	40.00	2023-07-16 16:49:49.519978	pcs	Organic Hair Care Oil
SKU-246252	Products2	Hair	Products	41.65	34.00	2023-07-16 16:50:55.284554	pcs	Arga Natural Wax Jars Promade Hair Grease
SKU-254916	Products3	Hair	Products	24.59	56.00	2023-07-16 16:52:10.03129	pcs	Botanical Butter Moisturizing Gel For Styling
SKU-838130	Kitchen1	Home and Living	Kitchen	67.90	78.00	2023-07-21 21:44:09.590465	pcs	4 Burner Gas Stoves
SKU-014572	Kitchen2	Home and Living	Kitchen	170.99	67.00	2023-07-21 21:45:36.063269	pcs	Cooker Hood with Chimney - Stainless Steel
SKU-819120	Kitchen3	Home and Living	Kitchen	12.80	80.00	2023-07-21 21:49:00.854923	pcs	Condiment Canisters Pots Set
SKU-175123	RoomDecoration1	Home and Living	Room Decoration	6.10	56.00	2023-07-21 22:17:19.604985	pcs	Mushroom Shaped Wall Mounted Rack
SKU-551824	RoomDecoration2	Home and Living	Room Decoration	7.90	79.00	2023-07-21 22:18:13.313363	pcs	Handmade Tulip Night Light
SKU-430667	RoomDecoration3	Home and Living	Room Decoration	23.40	49.00	2023-07-21 22:19:53.369399	pcs	Butterfly Design Wall Hanging Shelf
SKU-705914	GardenDesign1	Home and Living	Garden Design	13.40	46.00	2023-07-21 22:28:25.846858	pcs	Artificial Plant Topiary Ball
SKU-487423	GardenDesign2	Home and Living	Garden Design	14.90	58.00	2023-07-21 22:29:05.225829	pcs	Wooden Board Wall Hanging Decoration
SKU-332154	GardenDesign3	Home and Living	Garden Design	4.50	90.00	2023-07-21 22:31:42.535342	pcs	Miniature Garden Dwarfs
SKU-677207	RunningShoes1	Shoes	Running Shoes	230.99	89.00	2023-07-23 21:10:58.233866	pcs	Saucony Guide 14
SKU-565079	RunningShoes2	Shoes	Running Shoes	310.89	56.00	2023-07-23 21:11:41.881345	pcs	Unisex Trail Running Shoes
SKU-006618	RunningShoes3	Shoes	Running Shoes	190.00	87.00	2023-07-23 21:13:12.217762	pcs	HOKA Arahi 6
SKU-743130	Slippers1	Shoes	Slippers	23.39	67.00	2023-07-23 21:19:34.303543	pcs	Simple & Fashionable Home Slippers
SKU-003273	Slippers2	Shoes	Slippers	18.99	81.00	2023-07-23 21:20:17.604285	pcs	Simple Indoor Slippers
SKU-853678	Slippers3	Shoes	Slippers	19.00	45.00	2023-07-23 21:22:37.260911	pcs	Anti-skid Indoor Slippers
SKU-664360	Sneakers1	Shoes	Sneakers	130.40	74.00	2023-07-23 21:27:40.714117	pcs	Letter Graphic Sneakers
SKU-956650	Sneakers2	Shoes	Sneakers	160.79	56.00	2023-07-23 21:29:18.38109	pcs	Hook-and-loop Mesh Sneakers
SKU-514062	Sneakers3	Shoes	Sneakers	129.80	76.00	2023-07-23 21:30:18.37105	pcs	High Top Canvas Shoes
SKU-428146	Equipment1	Sports	Equipment	120.39	90.00	2023-07-27 21:58:27.584608	pcs	Drawstring Hooded Sports Set
SKU-717107	Equipment2	Sports	Equipment	89.00	76.00	2023-07-27 21:59:07.030485	pcs	3pcs Letter Tape Sports Set
SKU-892200	Equipment3	Sports	Equipment	134.00	53.00	2023-07-27 21:59:55.134535	pcs	Colorblock Running Set Workout Suit
SKU-809767	Shoes1	Sports	Shoes	190.99	98.00	2023-07-27 22:11:22.649192	pcs	RedTape White Sports Shoes
SKU-076080	Shoes2	Sports	Shoes	130.40	48.00	2023-07-27 22:12:34.77667	pcs	Men Running Shoes
SKU-847233	Shoes3	Sports	Shoes	187.00	73.00	2023-07-27 22:13:32.152311	pcs	Men Running Shoes
SKU-897801	SportAccessories1	Sports	Sport Accessories	10.30	45.00	2023-07-27 22:22:40.086343	pcs	Breathable Half-finger Fitness Gloves
SKU-469226	SportAccessories2	Sports	Sport Accessories	34.55	78.00	2023-07-27 22:24:17.960732	pcs	Freeride Ski Snowboard Backpack
SKU-235487	SportAccessories3	Sports	Sport Accessories	13.49	54.00	2023-07-27 22:25:21.328524	pcs	Two Tone Aqua Socks For Diving
\.


                                                                                                                                                       3043.dat                                                                                            0000600 0004000 0002000 00000004353 14463016231 0014250 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        SUBCAT-229422	Fruits	3	2023-05-26 23:49:16.464875	Food
SUBCAT-071375	Meat	3	2023-05-26 23:48:50.37785	Food
SUBCAT-374670	Men Shorts	3	2023-05-29 23:16:51.633328	Beachwear
SUBCAT-578736	Vegetables	3	2023-05-26 23:49:26.355061	Food
SUBCAT-121715	Accessories	3	2023-05-29 22:27:26.973575	Hair
SUBCAT-588893	Women Kimonos	3	2023-05-29 23:19:40.491781	Beachwear
SUBCAT-396877	Electrical Gadgets	3	2023-05-29 22:28:00.090327	Hair
SUBCAT-753978	Beach Shoes	3	2023-05-29 23:19:54.138523	Beachwear
SUBCAT-349058	Products	3	2023-05-29 22:28:25.351007	Hair
SUBCAT-946197	Kitchen	3	2023-05-29 22:28:39.436341	Home and Living
SUBCAT-099639	Horror	3	2023-05-28 22:54:34.005223	Books
SUBCAT-927949	Room Decoration	3	2023-05-29 22:29:23.441492	Home and Living
SUBCAT-001789	Garden Design	3	2023-05-29 22:29:46.033651	Home and Living
SUBCAT-132618	Romance	3	2023-05-29 22:14:58.038969	Books
SUBCAT-723612	Running Shoes	3	2023-05-29 22:30:11.413756	Shoes
SUBCAT-841352	Slippers	3	2023-05-29 22:30:27.204415	Shoes
SUBCAT-404203	Sneakers	3	2023-05-29 22:30:00.794406	Shoes
SUBCAT-411320	Documentary	3	2023-05-29 22:15:33.135204	Books
SUBCAT-289547	Equipment	3	2023-05-29 22:30:50.566951	Sports
SUBCAT-285245	Blouses	3	2023-05-29 22:19:54.858827	Clothes
SUBCAT-797933	Sunglasses	7	2023-05-26 23:54:16.151235	Accessories
SUBCAT-449528	Skirts	3	2023-05-29 22:20:11.835612	Clothes
SUBCAT-217393	Watches	3	2023-05-26 23:54:39.332132	Accessories
SUBCAT-717723	Shoes	3	2023-05-29 22:30:38.018158	Sports
SUBCAT-447460	Wallets	3	2023-05-26 23:54:56.457392	Accessories
SUBCAT-034132	Men Suits	3	2023-05-29 22:20:22.251715	Clothes
SUBCAT-777055	Sport Accessories	3	2023-05-29 22:31:04.599411	Sports
SUBCAT-344693	Makeup	3	2023-05-29 22:20:57.938804	Cosmetics
SUBCAT-082594	Nail Polish	3	2023-05-29 22:20:38.768112	Cosmetics
SUBCAT-144165	Skin Care Products	3	2023-05-29 22:21:10.524256	Cosmetics
SUBCAT-898267	Alcohol Beverages	3	2023-05-26 23:55:47.138864	Drinks
SUBCAT-701267	Non-Alcohol Beverages	3	2023-05-26 23:56:25.983667	Drinks
SUBCAT-642366	Coffee	3	2023-05-26 23:56:45.757214	Drinks
SUBCAT-841880	Photography Gadgets	3	2023-05-29 22:21:35.090624	Electronics
SUBCAT-576765	Computers	3	2023-05-29 22:25:48.232694	Electronics
SUBCAT-929950	Household Appliances	3	2023-05-29 22:26:59.482201	Electronics
\.


                                                                                                                                                                                                                                                                                     restore.sql                                                                                         0000600 0004000 0002000 00000022760 14463016231 0015373 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 13.11 (Debian 13.11-0+deb11u1)
-- Dumped by pg_dump version 13.11 (Debian 13.11-0+deb11u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE marketapp;
--
-- Name: marketapp; Type: DATABASE; Schema: -; Owner: alex
--

CREATE DATABASE marketapp WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE marketapp OWNER TO alex;

\connect marketapp

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: basket; Type: TABLE; Schema: public; Owner: raya
--

CREATE TABLE public.basket (
    username text NOT NULL,
    product_id text NOT NULL,
    product_name text NOT NULL,
    quantity numeric(10,2) NOT NULL,
    total_value smallint NOT NULL
);


ALTER TABLE public.basket OWNER TO raya;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: raya
--

CREATE TABLE public.categories (
    category_id text NOT NULL,
    category_name text NOT NULL,
    total_subcategories integer NOT NULL,
    total_items integer NOT NULL,
    last_modified timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    category_description text,
    category_function text,
    image_url text
);


ALTER TABLE public.categories OWNER TO raya;

--
-- Name: customers; Type: TABLE; Schema: public; Owner: raya
--

CREATE TABLE public.customers (
    customer_id bigint NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email_address text NOT NULL,
    phone text NOT NULL,
    registration_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    username text,
    total_orders integer
);


ALTER TABLE public.customers OWNER TO raya;

--
-- Name: employees; Type: TABLE; Schema: public; Owner: raya
--

CREATE TABLE public.employees (
    employee_id smallint NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email_address character varying(30) NOT NULL,
    phone text NOT NULL
);


ALTER TABLE public.employees OWNER TO raya;

--
-- Name: favourite_products; Type: TABLE; Schema: public; Owner: alex
--

CREATE TABLE public.favourite_products (
    username character varying(50),
    product_id character varying(10),
    product_name character varying(50)
);


ALTER TABLE public.favourite_products OWNER TO alex;

--
-- Name: orders; Type: TABLE; Schema: public; Owner: raya
--

CREATE TABLE public.orders (
    order_id text NOT NULL,
    username text NOT NULL,
    product_id text NOT NULL,
    product_name text NOT NULL,
    single_price numeric(10,2) NOT NULL,
    quantity numeric(10,2) NOT NULL,
    total_value numeric(10,2) GENERATED ALWAYS AS ((single_price * quantity)) STORED,
    date_ordered timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.orders OWNER TO raya;

--
-- Name: payment_options; Type: TABLE; Schema: public; Owner: alex
--

CREATE TABLE public.payment_options (
    payment_code text NOT NULL,
    payment_name text,
    payment_type text,
    card_number text,
    card_holder text,
    ccv numeric,
    expire_date date,
    default_option boolean,
    username text
);


ALTER TABLE public.payment_options OWNER TO alex;

--
-- Name: products; Type: TABLE; Schema: public; Owner: alex
--

CREATE TABLE public.products (
    product_id text NOT NULL,
    product_name text NOT NULL,
    category text NOT NULL,
    subcategory text NOT NULL,
    single_price numeric(10,2) NOT NULL,
    quantity numeric(10,2) NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    total_value numeric(10,2) GENERATED ALWAYS AS ((single_price * quantity)) STORED,
    unit_of_measure text,
    product_description character varying
);


ALTER TABLE public.products OWNER TO alex;

--
-- Name: subcategories; Type: TABLE; Schema: public; Owner: raya
--

CREATE TABLE public.subcategories (
    subcategory_id text NOT NULL,
    subcategory_name text NOT NULL,
    total_items integer NOT NULL,
    last_modified timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    parent_category text
);


ALTER TABLE public.subcategories OWNER TO raya;

--
-- Data for Name: basket; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.basket (username, product_id, product_name, quantity, total_value) FROM stdin;
\.
COPY public.basket (username, product_id, product_name, quantity, total_value) FROM '$$PATH$$/3047.dat';

--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.categories (category_id, category_name, total_subcategories, total_items, last_modified, category_description, category_function, image_url) FROM stdin;
\.
COPY public.categories (category_id, category_name, total_subcategories, total_items, last_modified, category_description, category_function, image_url) FROM '$$PATH$$/3042.dat';

--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.customers (customer_id, first_name, last_name, email_address, phone, registration_date, username, total_orders) FROM stdin;
\.
COPY public.customers (customer_id, first_name, last_name, email_address, phone, registration_date, username, total_orders) FROM '$$PATH$$/3040.dat';

--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.employees (employee_id, first_name, last_name, email_address, phone) FROM stdin;
\.
COPY public.employees (employee_id, first_name, last_name, email_address, phone) FROM '$$PATH$$/3041.dat';

--
-- Data for Name: favourite_products; Type: TABLE DATA; Schema: public; Owner: alex
--

COPY public.favourite_products (username, product_id, product_name) FROM stdin;
\.
COPY public.favourite_products (username, product_id, product_name) FROM '$$PATH$$/3046.dat';

--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.orders (order_id, username, product_id, product_name, single_price, quantity, date_ordered) FROM stdin;
\.
COPY public.orders (order_id, username, product_id, product_name, single_price, quantity, date_ordered) FROM '$$PATH$$/3048.dat';

--
-- Data for Name: payment_options; Type: TABLE DATA; Schema: public; Owner: alex
--

COPY public.payment_options (payment_code, payment_name, payment_type, card_number, card_holder, ccv, expire_date, default_option, username) FROM stdin;
\.
COPY public.payment_options (payment_code, payment_name, payment_type, card_number, card_holder, ccv, expire_date, default_option, username) FROM '$$PATH$$/3045.dat';

--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: alex
--

COPY public.products (product_id, product_name, category, subcategory, single_price, quantity, date_created, unit_of_measure, product_description) FROM stdin;
\.
COPY public.products (product_id, product_name, category, subcategory, single_price, quantity, date_created, unit_of_measure, product_description) FROM '$$PATH$$/3044.dat';

--
-- Data for Name: subcategories; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.subcategories (subcategory_id, subcategory_name, total_items, last_modified, parent_category) FROM stdin;
\.
COPY public.subcategories (subcategory_id, subcategory_name, total_items, last_modified, parent_category) FROM '$$PATH$$/3043.dat';

--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: raya
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (category_id);


--
-- Name: customers customers_customer_id_key; Type: CONSTRAINT; Schema: public; Owner: raya
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_customer_id_key UNIQUE (customer_id);


--
-- Name: employees employees_employee_id_key; Type: CONSTRAINT; Schema: public; Owner: raya
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_employee_id_key UNIQUE (employee_id);


--
-- Name: payment_options payment_options_pkey; Type: CONSTRAINT; Schema: public; Owner: alex
--

ALTER TABLE ONLY public.payment_options
    ADD CONSTRAINT payment_options_pkey PRIMARY KEY (payment_code);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: alex
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- Name: subcategories subcategories_pkey; Type: CONSTRAINT; Schema: public; Owner: raya
--

ALTER TABLE ONLY public.subcategories
    ADD CONSTRAINT subcategories_pkey PRIMARY KEY (subcategory_id);


--
-- Name: DATABASE marketapp; Type: ACL; Schema: -; Owner: alex
--

GRANT ALL ON DATABASE marketapp TO raya;
GRANT ALL ON DATABASE marketapp TO bobby;


--
-- Name: TABLE customers; Type: ACL; Schema: public; Owner: raya
--

GRANT SELECT,UPDATE ON TABLE public.customers TO customers_marketapp;


--
-- Name: TABLE employees; Type: ACL; Schema: public; Owner: raya
--

GRANT SELECT,UPDATE ON TABLE public.employees TO customers_marketapp;


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
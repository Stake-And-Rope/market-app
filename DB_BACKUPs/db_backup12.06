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

SET default_tablespace = '';

SET default_table_access_method = heap;

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
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.categories (category_id, category_name, total_subcategories, total_items, last_modified, category_description, category_function, image_url) FROM stdin;
CAT-795326	Clothes	6	0	2023-05-19 11:53:43.813573	Have your new clothes from here!	clothes	https://images.app.goo.gl/WNEcwoMLLNnu6R238
CAT-821620	Accessories	3	13	2023-05-19 12:15:16.17974	All kind of accessories here!	accessories	https://images.app.goo.gl/Qk242WM6hBe56aCQ6
CAT-314816	Cosmetics	3	0	2023-05-19 11:55:21.893555	Cosmetics for everyone!	cosmetics	https://images.app.goo.gl/UWwsxuuG7NKNR4Hv5
CAT-177703	Electronics	3	0	2023-05-19 12:05:45.844296	Find everything you need for your computer and others!	electronics	https://images.app.goo.gl/3XVce8jEJ2aChiQU8
CAT-363803	Hair	3	0	2023-05-19 12:24:00.685837	Many healthy things for your hair here!	hair	https://images.app.goo.gl/f5nvEDph1yzURHwb7
CAT-181291	Home and Living	3	0	2023-05-19 11:56:32.928574	Everything for your home!	homeandliving	https://images.app.goo.gl/UkpEkbCuS5oCVEVh9
CAT-239320	Food	3	0	2023-05-19 11:50:36.503393	Find whatever you like eating here!	food	https://images.app.goo.gl/4H8yYtfftKY3vFev6
CAT-584109	Shoes	3	0	2023-05-19 12:10:57.61498	Every different kind of shoes here!	shoes	https://images.app.goo.gl/ENETVsfDjkC86yVm9
CAT-953732	Drinks	3	0	2023-05-19 11:51:37.197437	Find all drinks here!	drinks	https://images.app.goo.gl/1kr39sC5ryKSFcfB7
CAT-375354	Sports	3	0	2023-05-19 12:23:23.711324	Find shoes, clothes and many others for your sport here!	sports	https://images.app.goo.gl/CBvbUGM88dswuwto9
CAT-872552	Books	3	0	2023-05-19 11:52:52.477528	Read all the books we have!	books	https://images.app.goo.gl/y898YQTGFXn5mCv59
CAT-360035	Beachwear	6	0	2023-05-19 12:16:45.248848	Anything for the beach you can find is here!	beachwear	https://images.app.goo.gl/UNgzBfepKswJRQwL8
\.


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.customers (customer_id, first_name, last_name, email_address, phone, registration_date, username, total_orders) FROM stdin;
8788935163	Pesho	Peshev	pesho@example.com	555-123-321	2023-05-27 14:32:17.00807	pesho	0
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.employees (employee_id, first_name, last_name, email_address, phone) FROM stdin;
\.


--
-- Data for Name: payment_options; Type: TABLE DATA; Schema: public; Owner: alex
--

COPY public.payment_options (payment_code, payment_name, payment_type, card_number, card_holder, ccv, expire_date, default_option, username) FROM stdin;
PAY-123456	My-Visa	[Visa]	XXXX-XXX-1234	Pesho Peshev	123	2025-06-11	t	pesho
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: alex
--

COPY public.products (product_id, product_name, category, subcategory, single_price, quantity, date_created, unit_of_measure, product_description) FROM stdin;
SKU-025512	Sunglasses1	Accessories	Sunglasses	45.99	41.00	2023-06-10 21:08:57.871275	pcs	Men Solid Wrap Fashion Glasses For Daily Decoration
SKU-859357	Sunglasses2	Accessories	Sunglasses	34.50	59.00	2023-06-10 21:14:25.476657	pcs	Geometric Frame Black Fashion Glasses
SKU-778002	Sunglasses3	Accessories	Sunglasses	50.99	30.00	2023-06-10 21:15:42.356198	pcs	Women Geometric Frame Boho Fashion Glasses For Outdoor
SKU-708855	Watches2	Accessories	Watches	230.89	46.00	2023-06-10 21:34:01.955891	pcs	Men Black Nylon Strap Casual Round Watch
SKU-323357	Watches3	Accessories	Watches	189.99	58.00	2023-06-10 21:34:59.124787	pcs	Mesh Strap Round Pointer Quartz Watch
SKU-612016	Wallet1	Accessories	Wallets	50.75	34.00	2023-06-10 21:38:43.870206	pcs	Crocodile Embossed Flap Small Wallet
SKU-269114	Wallet2	Accessories	Wallets	78.99	55.00	2023-06-10 21:39:52.112009	pcs	Men Letter Graphic Small Wallet
SKU-525292	Wallet3	Accessories	Wallets	45.89	38.00	2023-06-10 21:40:43.901692	pcs	Letter Graphic Small Pocket Wallet
SKU-269217	Watches1	Accessories	Watches	120.99	37.00	2023-06-10 21:33:01.634615	pcs	Women White PU Polyurethane Strap Elegant Watch
\.


--
-- Data for Name: subcategories; Type: TABLE DATA; Schema: public; Owner: raya
--

COPY public.subcategories (subcategory_id, subcategory_name, total_items, last_modified, parent_category) FROM stdin;
SUBCAT-071375	Meat	0	2023-05-26 23:48:50.37785	Food
SUBCAT-229422	Fruits	0	2023-05-26 23:49:16.464875	Food
SUBCAT-578736	Vegetables	0	2023-05-26 23:49:26.355061	Food
SUBCAT-898267	Alcohol Beverages	0	2023-05-26 23:55:47.138864	Drinks
SUBCAT-701267	Non-Alcohol Beverages	0	2023-05-26 23:56:25.983667	Drinks
SUBCAT-642366	Coffee	0	2023-05-26 23:56:45.757214	Drinks
SUBCAT-099639	Horror	0	2023-05-28 22:54:34.005223	Books
SUBCAT-132618	Romance	0	2023-05-29 22:14:58.038969	Books
SUBCAT-411320	Documentary	0	2023-05-29 22:15:33.135204	Books
SUBCAT-285245	Blouses	0	2023-05-29 22:19:54.858827	Clothes
SUBCAT-449528	Skirts	0	2023-05-29 22:20:11.835612	Clothes
SUBCAT-034132	Men Suits	0	2023-05-29 22:20:22.251715	Clothes
SUBCAT-082594	Nail Polish	0	2023-05-29 22:20:38.768112	Cosmetics
SUBCAT-344693	Makeup	0	2023-05-29 22:20:57.938804	Cosmetics
SUBCAT-144165	Skin Care Products	0	2023-05-29 22:21:10.524256	Cosmetics
SUBCAT-841880	Photography Gadgets	0	2023-05-29 22:21:35.090624	Electronics
SUBCAT-576765	Computers	0	2023-05-29 22:25:48.232694	Electronics
SUBCAT-929950	Household Appliences	0	2023-05-29 22:26:59.482201	Electronics
SUBCAT-121715	Accessories	0	2023-05-29 22:27:26.973575	Hair
SUBCAT-396877	Electric Gadgets	0	2023-05-29 22:28:00.090327	Hair
SUBCAT-349058	Products	0	2023-05-29 22:28:25.351007	Hair
SUBCAT-946197	Kitchen	0	2023-05-29 22:28:39.436341	Home and Living
SUBCAT-927949	Room Decoration	0	2023-05-29 22:29:23.441492	Home and Living
SUBCAT-001789	Garden Design	0	2023-05-29 22:29:46.033651	Home and Living
SUBCAT-404203	Sneakers	0	2023-05-29 22:30:00.794406	Shoes
SUBCAT-723612	Running Shoes	0	2023-05-29 22:30:11.413756	Shoes
SUBCAT-841352	Slippers	0	2023-05-29 22:30:27.204415	Shoes
SUBCAT-717723	Shoes	0	2023-05-29 22:30:38.018158	Sports
SUBCAT-289547	Equipment	0	2023-05-29 22:30:50.566951	Sports
SUBCAT-777055	Sport Accessories	0	2023-05-29 22:31:04.599411	Sports
SUBCAT-374670	Men Shorts	0	2023-05-29 23:16:51.633328	Beachwear
SUBCAT-588893	Women Kimonos	0	2023-05-29 23:19:40.491781	Beachwear
SUBCAT-753978	Beach Shoes	0	2023-05-29 23:19:54.138523	Beachwear
SUBCAT-797933	Sunglasses	7	2023-05-26 23:54:16.151235	Accessories
SUBCAT-217393	Watches	3	2023-05-26 23:54:39.332132	Accessories
SUBCAT-447460	Wallets	3	2023-05-26 23:54:56.457392	Accessories
\.


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


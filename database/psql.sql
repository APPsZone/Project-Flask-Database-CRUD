PGDMP     -                    y            Garage    13.2    13.2     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    24808    Garage    DATABASE     l   CREATE DATABASE "Garage" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "Garage";
                postgres    false            ?            1259    33125 	   aksesoris    TABLE     ?   CREATE TABLE public.aksesoris (
    id integer NOT NULL,
    namabarang character varying(30) NOT NULL,
    harga character varying(256) NOT NULL,
    stok character varying(256) NOT NULL
);
    DROP TABLE public.aksesoris;
       public         heap    postgres    false            ?            1259    33123    aksesoris_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.aksesoris_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.aksesoris_id_seq;
       public          postgres    false    206            ?           0    0    aksesoris_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.aksesoris_id_seq OWNED BY public.aksesoris.id;
          public          postgres    false    205            ?            1259    33109 
   jasaservis    TABLE     ?   CREATE TABLE public.jasaservis (
    id integer NOT NULL,
    nama character varying(60) NOT NULL,
    harga character varying(256) NOT NULL
);
    DROP TABLE public.jasaservis;
       public         heap    postgres    false            ?            1259    33107    jasaservis_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.jasaservis_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.jasaservis_id_seq;
       public          postgres    false    203            ?           0    0    jasaservis_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.jasaservis_id_seq OWNED BY public.jasaservis.id;
          public          postgres    false    202            ?            1259    33115 	   sparepart    TABLE     ?   CREATE TABLE public.sparepart (
    part character varying(30) NOT NULL,
    harga character varying(256) NOT NULL,
    stok character varying(256) NOT NULL
);
    DROP TABLE public.sparepart;
       public         heap    postgres    false            ?            1259    33050    users    TABLE     ?   CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(25) NOT NULL,
    password text NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            ?            1259    33056    users_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.users_id_seq;
       public          postgres    false    200            ?           0    0    users_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;
          public          postgres    false    201            7           2604    33128    aksesoris id    DEFAULT     l   ALTER TABLE ONLY public.aksesoris ALTER COLUMN id SET DEFAULT nextval('public.aksesoris_id_seq'::regclass);
 ;   ALTER TABLE public.aksesoris ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    206    205    206            6           2604    33112    jasaservis id    DEFAULT     n   ALTER TABLE ONLY public.jasaservis ALTER COLUMN id SET DEFAULT nextval('public.jasaservis_id_seq'::regclass);
 <   ALTER TABLE public.jasaservis ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    202    203    203            5           2604    33105    users id    DEFAULT     d   ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);
 7   ALTER TABLE public.users ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    201    200            ?          0    33125 	   aksesoris 
   TABLE DATA           @   COPY public.aksesoris (id, namabarang, harga, stok) FROM stdin;
    public          postgres    false    206   ~       ?          0    33109 
   jasaservis 
   TABLE DATA           5   COPY public.jasaservis (id, nama, harga) FROM stdin;
    public          postgres    false    203   ?       ?          0    33115 	   sparepart 
   TABLE DATA           6   COPY public.sparepart (part, harga, stok) FROM stdin;
    public          postgres    false    204   ?       ?          0    33050    users 
   TABLE DATA           7   COPY public.users (id, username, password) FROM stdin;
    public          postgres    false    200   ?       ?           0    0    aksesoris_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.aksesoris_id_seq', 1, false);
          public          postgres    false    205            ?           0    0    jasaservis_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.jasaservis_id_seq', 1, false);
          public          postgres    false    202            ?           0    0    users_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.users_id_seq', 7, true);
          public          postgres    false    201            ?           2606    33133    aksesoris aksesoris_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.aksesoris
    ADD CONSTRAINT aksesoris_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.aksesoris DROP CONSTRAINT aksesoris_pkey;
       public            postgres    false    206            =           2606    33114    jasaservis jasaservis_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.jasaservis
    ADD CONSTRAINT jasaservis_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.jasaservis DROP CONSTRAINT jasaservis_pkey;
       public            postgres    false    203            9           2606    33071    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    200            ;           2606    33073    users users_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public.users DROP CONSTRAINT users_username_key;
       public            postgres    false    200            ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?   e  x?m?As?0???wp?Q@?Ŋ??"-?^??h"?__k=?fv???췆R????~?h????`wc젾&@@q??q??Ctm?$(8A7??4?y?SI+?OTi??D??Ś??N??N'??#2L?px?????a?wG?(?qo}>_??]?e?xj6i6??n?M?rz???55U?c>?G?W????5???fi?????^K??s?.????'????Ȍ?????y??:^?L`????b+?????;{??rz??
??.-???#??@?????-bEL??Eh?q??f_????<????a{F[?? ???'?)??S)?%	??z?Y???y%???.??X???軇?j??2     
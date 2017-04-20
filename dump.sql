--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.5
-- Dumped by pg_dump version 9.5.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: analyses; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE analyses (
    analyses_id integer NOT NULL,
    user_id integer NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    tweet_sent_id integer NOT NULL,
    quote_id integer NOT NULL
);


ALTER TABLE analyses OWNER TO vagrant;

--
-- Name: analyses_analyses_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE analyses_analyses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE analyses_analyses_id_seq OWNER TO vagrant;

--
-- Name: analyses_analyses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE analyses_analyses_id_seq OWNED BY analyses.analyses_id;


--
-- Name: classifier; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE classifier (
    classifier_id integer NOT NULL,
    tweet_content character varying(300) NOT NULL,
    test_or_train character varying(10) NOT NULL,
    sentiment_id integer NOT NULL
);


ALTER TABLE classifier OWNER TO vagrant;

--
-- Name: classifier_classifier_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE classifier_classifier_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE classifier_classifier_id_seq OWNER TO vagrant;

--
-- Name: classifier_classifier_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE classifier_classifier_id_seq OWNED BY classifier.classifier_id;


--
-- Name: quotes; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE quotes (
    quote_id integer NOT NULL,
    content text,
    img_url text,
    author character varying(50),
    sentiment_id integer NOT NULL
);


ALTER TABLE quotes OWNER TO vagrant;

--
-- Name: quotes_quote_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE quotes_quote_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE quotes_quote_id_seq OWNER TO vagrant;

--
-- Name: quotes_quote_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE quotes_quote_id_seq OWNED BY quotes.quote_id;


--
-- Name: sentiments; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE sentiments (
    sentiment_id integer NOT NULL,
    sentiment character varying(15) NOT NULL
);


ALTER TABLE sentiments OWNER TO vagrant;

--
-- Name: sentiments_sentiment_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE sentiments_sentiment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE sentiments_sentiment_id_seq OWNER TO vagrant;

--
-- Name: sentiments_sentiment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE sentiments_sentiment_id_seq OWNED BY sentiments.sentiment_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE users (
    user_id integer NOT NULL,
    user_name character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    twitter_handle character varying(50) NOT NULL,
    email character varying(50) NOT NULL,
    phone character varying,
    reminder_time character varying(20)
);


ALTER TABLE users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;


--
-- Name: analyses_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY analyses ALTER COLUMN analyses_id SET DEFAULT nextval('analyses_analyses_id_seq'::regclass);


--
-- Name: classifier_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY classifier ALTER COLUMN classifier_id SET DEFAULT nextval('classifier_classifier_id_seq'::regclass);


--
-- Name: quote_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY quotes ALTER COLUMN quote_id SET DEFAULT nextval('quotes_quote_id_seq'::regclass);


--
-- Name: sentiment_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY sentiments ALTER COLUMN sentiment_id SET DEFAULT nextval('sentiments_sentiment_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);


--
-- Data for Name: analyses; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY analyses (analyses_id, user_id, "timestamp", tweet_sent_id, quote_id) FROM stdin;
4	1	2017-01-09 01:42:00	1	2
5	1	2017-01-10 01:42:00	1	18
6	1	2017-01-11 01:42:00	1	3
7	1	2017-01-12 01:42:00	1	24
8	1	2017-01-13 01:42:00	1	11
9	1	2017-01-14 01:42:00	1	4
10	1	2017-01-15 01:42:00	1	25
11	1	2017-01-16 01:42:00	1	23
12	1	2017-01-17 01:42:00	1	27
13	1	2017-01-18 01:42:00	1	6
14	1	2017-01-19 01:42:00	1	8
15	1	2017-01-25 01:42:00	1	9
16	1	2017-01-30 01:42:00	1	28
17	1	2017-02-04 01:42:00	1	29
18	1	2017-02-05 01:42:00	2	56
19	1	2017-02-10 01:42:00	2	70
20	1	2017-02-14 01:42:00	2	46
28	1	2017-03-11 01:42:00	2	34
29	1	2017-03-12 01:42:00	2	31
1	1	2017-01-06 01:32:00	2	44
3	1	2017-01-08 01:42:00	2	5
30	1	2017-04-12 01:17:52	1	17
108	1	2017-04-20 15:50:50	1	239
\.


--
-- Name: analyses_analyses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('analyses_analyses_id_seq', 108, true);


--
-- Data for Name: classifier; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY classifier (classifier_id, tweet_content, test_or_train, sentiment_id) FROM stdin;
1	actors kiss each other for like 10 seasons and dont fall in love but when someone holds the door for me i think about it for like 5 months	test	1
2	Thank you so much to my fans and friends for making Million Reasons a hit! #4 on the Billboard Hot 100! I believe in this song so much	test	1
3	7 years since launching #letsmove, so proud of what we've done to support healthy families. More to do! http://bit.ly/2lE3OaA 	test	1
4	Happy Valentine’s Day, @michelleobama! Almost 28 years with you, but it always feels new.	test	1
5	.@MsJamieBrewer thank you for joining me tonight to celebrate the voice finale ! Love uuuuu	test	1
6	hi  Just wanted to say I'm grateful for your love and support every day of my life, not just…	test	1
7	Today, just telling the truth and having integrity is revolutionary, subversive, and counter-cultural.	test	1
8	OHT for today! 😁  #EncantadiaPalaisipan Soooo excited ❤ 😍	test	1
9	A gorgeous day for #LeanStartup Week! Congrats to @UrbanitySF @melissazmoore and team for making it happen!	test	1
10	Hate is a desperate thing. That is why we are seeing the world this way. But LOVE? Yeah man. LOVE is like cream. It always rises to the top.	test	1
11	Wavy baby 🌊 Sooooooo much talent from the Chi I swear it seems unfair 👀  😱  #Bars 😂 😂 😂 💋 💋 💋 	test	1
12	Love 'em. Wish there were more of 'em.	test	1
13	YASSSS	test	1
14	Still totally surreal ! I ❤️  @NPRCodeSwitch and @RadioMirage	test	1
15	Proud of you Spurs! But Leicester... What an inspiration, the best fucking story ever! Congratulations!!!! X	test	1
16	Throwing it way back with this! Thank you for all the love, I am so blown away. X  #TBT	test	1
17	Kick some ass today @ladygaga Xoxox #SuperBowl #HalfTimeShow #LadyGaga	test	1
18	Wow!the vibes are so good in the morning 😊	test	1
19	Had a special day today with my birthday boy. Thanks for all the lovely messages !	test	1
20	My lover boy ❤	test	1
21	I love DJ James so much I can't explain. I appreciate the entertainment so, so much. I love you.	test	1
22	misses Jason really bad	test	2
23	misses playing LotRO	test	2
24	misses school what to do for a week's vacation? :-?	test	2
25	misses Tal already.... it's going to be a long summer	test	2
26	Misses the DB crew	test	2
27	Misses the JIM! Tuesday evening, please hurry on up	test	2
28	misses Vegan food	test	2
29	when you think its gonna be a shitty day and you were right	test	2
30	One minute they love you and the next minute they hate you.	test	2
31	My heart absolutely breaks for Haiti  !!! Prayers up for my brothers and sisters who've fallen victim to this tragic event!	test	2
32	I took a tragic horrific experience and did not let it diminish me, rather grew and evolved and allowed the experience to teach me.	test	2
33	When I get mad, I'm really angry.. only because It stems from the build up that I haven't released.	test	2
34	So sad that we are in the 21st century yet people still kill each other for cattle. Nothing is worth human life!!	test	2
35	such a sad news. goosebumps all over me 😣	test	2
36	now i'm sad goodnight	test	2
37	when ur being annoying and u know ur being annoying so u apologize for being annoying and now ur even more annoying	test	2
38	"Are they friends of yours?" 😡 😭 😱 😤 😓  really trump?!?? #trumpsoracist #dumptrump	test	2
39	The fastest way to melt glaciers & flood the World's coastal cities: Ignore scientists and do nothing to stem the rise of CO2	test	2
40	I got out of the car and was like phew that was kind of a boring day anyhow.	test	2
41	We're barely aqquaintences and you're still trying to use me.	test	2
42	Always get stuck next to the drunk, swaying girl #NeverFails	test	2
43	I don't feel great. I lived too mas last night.	test	2
44	Still in shock over this -- and yes I get to be shocked by awful behavior. Will not accept the death of decency	test	2
45	when u see your friends prospering and you just watching happy to see them flourish	train	1
46	Happy first kiss anniversary to the most beautiful first kiss. Long live to Malec	train	1
47	I want to whine but nah~ Dara is happy, I am happy too. #원스텝VIPPremiere	train	1
48	So so happy to be back in my favorite city in the world. Love you LDN! 🇬🇧 🍺	train	1
49	Be happy. Be who you want to be. If others don't like it, then let them be. Happiness is a choice. Life isn't about pleasing everybody.	train	1
50	I am a strong black woman. I cannot be intimidated, and I'm not going anywhere. #BlackWomenAtWork	train	1
51	I'am a strong person, because I know my weaknesses. I'am wise because I learn from my mistakes I can laugh, because I have known sadness	train	1
52	i'm obsessed with my space & alone time so if i wanna spend time with you or talk to you consistently, just know you're special	train	1
53	i'm not perfect, but i'm loyal af	train	1
54	Sometimes you have to go through the worst in order to get to the best.	train	1
55	Dear God, thanks for everything.	train	1
56	really loved how dara was ecstatic when she saw people who went to give her support  my girl deserves their love #원스텝VIPPremiere	train	1
57	Ecstatic to say that I've verbally committed to play volleyball at Montreat College. Go cavs!!	train	1
58	i'm really excited for monsta x on weekly idol because they already look super extra and funny	train	1
59	Nice to see you again coach @MsLeaSalonga !!! 👍 😘  ❤ 🙏	train	1
60	ZOMG this sounds amazing. Preview is 🔥 🔥 🔥	train	1
61	Such a great event! Thank you @Startup_TOR for organizing! #iwd 	train	1
62	Democrats will filibuster the nomination of Neil Gorsuch, Trump’s Supreme Court pick. YEAAASSSSSSSS. #RESIST	train	1
63	I've always loved SNL, but I swear @ColinJost and Michael Che's @SNLUpdate are what keep me happy and laughing into each scary week of 2017	train	1
258	i want a hug	train	2
64	What a great pairing! @georgezimmer of Men’s Wearhouse and Tom Montgomery of @chubbies #hustlecon	train	1
65	Super exciting - predictive biomarkers could potentially fill a major gap in strategies to combat brain degeneration! 	train	1
66	The most uplifting and triumphant movie of the year. #HiddenFigures is now available on Digital HD.	train	1
67	We salute these powerful women each and every day.	train	1
68	😎 💋 💋 💋	train	1
69	☀️💋	train	1
70	🚿 🙏🏾 💆🏽 😊 💋 💋 💋  	train	1
71	#Empire 💪🏾 💋 💋 💋	train	1
72	Nooooooooooooooooooooo #Cookie and the crowd goes wild. 😂 😂 😂 😂 😂 💆🏽  #Empire	train	1
73	Yes @TherealTaraji and this scene 🔥 🔥 🔥 🔥 YES!!! Tear this ish up #Cookie DNA all up and thru #Empire	train	1
74	Cookie so bold. I LOVE IT!! #Empire  @TherealTaraji	train	1
75	😍 😍 😍 💋 💋 💋	train	1
76	TONIGHT IT IS GOING DOWN!!! I am soooooooooo excited for my sister @octaviaspencer I love you… 	train	1
77	Y'all have a best day. Be LOVE.	train	1
78	It can get overwhelming. No time. Don't get buried under the things that do not matter. Frivolous beefs, whether he tweets,etc. Look deeper.	train	1
79	Every day is a great day. Our job is to discover what is great about it.	train	1
80	Ian Grillot, you are best of humanity. I learned so much from you courageous actions. @indiahouse, bravo.	train	1
81	slay Ethan Coen slay	train	1
82	Senator, if Mindy Lahiri shades it, it means we know it's cool. Thanks for the ❤. It's mutual!	train	1
83	I like a good celeb sighting	train	1
84	I have so much admiration for @PreetBharara.	train	1
85	With @XoshaRockstar, Beyoncé, Amal, if 2017 brings us anything it's some quality babies. Congratulations to my gorgeous, hilarious friend.	train	1
86	One of the best musicals ever that so few know about. Fantastic documentary about the original Broadway production of #merrilywerollalong	train	1
87	I like you, Moana girl, you hella likable	train	1
88	Oh hi Dev Patel's mom, I see you and you are the worlds cutest person	train	1
89	I like that work ethic! Thanks for watching! 😉	train	1
90	I see you and I love you back. Happy birthday, cool youngster I hope I meet some day! 😍 ❤	train	1
91	This performance is like 4000 awesome gifs strung together	train	1
92	Hi @mykeltiwmson! Congratulations on your beautiful performance in #FencesMovie. You deserve every award. ❤❤❤	train	1
93	Thank you @BarackObama. Can't wait to see what's next. ❤	train	1
94	I haven't been so moved and entertained as I was watching #Hiddenfigures. It's a movie for the ambitious and the underestimated. A must see!	train	1
95	Let's all talk about how Dev Patel is super hot	train	1
96	Best ever	train	1
97	 Merry Christmas @BethGrantActor, and thanks for the present of @jackiefilm ❤❤	train	1
98	So excited for this, why must I wait so long? ❤️ ❤️ ❤️	train	1
99	Thank u @YaraShahidi for instroducing me to this song... I'm obsessed! #FrankOcean #Chanel	train	1
100	I love u Mom @DianaRoss! Happy Birthday!	train	1
101	“A feminist is anyone who recognizes the equality and full humanity of women and men.” Happy birthday to the extraordinary @GloriaSteinem!	train	1
102	Best thing ever. When you get to play sisters with your friends. @iamrashidajones #blackish	train	1
103	Good morning! It's all still here!	train	1
104	@DuaneJackson lol, love it when that happens. Go do it...	train	1
105	@DuaneJackson weather kinda sux atm but its the weekend, that's always something to smile about	train	1
106	It's okay! We had movie day :)	train	1
107	Major major @Adele respects. Shit happens when you actually sing live. She was incredible.	train	1
108	YES Gaga!!	train	1
109	SISTERHOOD	train	1
110	Lady you SMASHED it! Totally nailed it 👌🏻	train	1
111	I need to share with you all that I am eating the best burrito of my life. It is an explosively joyous moment	train	1
112	I had the best time doing this! We met 7 years ago in an aeroplane hanger in Wales!! Love you mate @JKCorden X	train	1
113	So...tonight was THE best night of my life. I love you Stevie Nicks!! The queen of melodies! Thanks for everything x	train	1
114	Thank you for the birthday wishes I had a wonderful time! I was my hero x #gottahavefaith	train	1
115	Just wanted to wish everyone happy holidays & all the best for 2015! PS Simon & I are still very much together, don't believe what you readx	train	1
116	It's charming, devastating, gives you butterflies, totally amazingly fairy tale like but living in South London grimey but glitzy	train	1
117	I passed my driving test this morning!!! 💪 🎉 🎈 🚗 🚦	train	1
118	and we're home! What an epic trip. Thanks for having us Hollywood!	train	1
119	Thank you to everyone who saw our film Beauty and the Beast! I saw so many lovely photos of families at the cinema together! Love, Em x ❤️🌹	train	1
120	Today I am going to deliver Maya Angelou books to the New York subway. Then I am going to fight even harder for all the things I believe in.	train	1
121	Happy birthday, @LadyGaga! It’s been 31 years since you emerged from your giant egg, and we couldn’t be happier about it.	train	1
122	Stepping your feet in the ocean is healing	train	1
123	Who's excited about this new record ? Cause.... I AM!!!!!!! #writing #recording	train	1
124	Thanks Danica for the sweet children's bedtime book for my nephew!!! #GoodnightNumbers by @danicamckellar makes a great gift :)	train	1
125	Ya!!!!	train	1
126	I challenged myself as a songwriter & I wanted to write about topics I hadn't hit on before Check the rest of my interview on @billboard!	train	1
127	Incredibly excited to be a part of the @BMG_US family & be working with them on the release of #AL6! So excited to share more with you guys!	train	1
351	Misses them already..wishes they would of invited me to stay the night	train	2
128	Congrats to my little sister Michelle and Ryota on their marriage! Wishing you both all the love and happiness in the world! ❤  #family #love	train	1
129	In honor of #NationalPizzaDay I'm posting a shot from my FAVORITE pizza spot La Pizzaria in Napanee Ontario. I always pop in when I'm home!	train	1
130	Wow. Awesome!	train	1
131	I won't bow I won't break #warrior #newlyricalert #AL6	train	1
132	Touched you found strength in my music. Thank you.	train	1
133	I say yes to health, wealth, happiness and wholeness throughout the day! And it says yes right back!	train	1
134	Today I close my mouth & open my heart & mind & Guidance from the Divine!	train	1
135	I Am a joyously loving & kind expression of Spirit so today, I make sure my words and actions reflect this truth,	train	1
136	Today, let's look friends and give thanks for the love, sharing, kindness, fun and more! I'm grateful to them!	train	1
137	Today was an important day of the semester for me. I'm happy to say I'm back on track to where I want to be 😍	train	1
138	I can already tell that I'm going to be in love with the new @FIROfficial album. All 3 songs released so far are 🔥 🔥 🔥	train	1
139	TBH ion care what people got to say bout my size .....I love my thick thighs 👑 .   My lil tummy ❤️ #thickgirlpositivity	train	1
140	Honestly too fucking excited for tomorrow !! 😝 😝 😝 😝 😝	train	1
141	Still buzzing about the brit award ! Love !!	train	1
142	Loads and loads of love !!!	train	1
143	Looking forward to some English food !	train	1
144	It's been too long ! @JKCorden . Can't wait to see you mate	train	1
145	Nothing more relaxing in the world than cuddling my Freddie :)	train	1
146	Reading through so many lovely messages after tonight's performance . Thank you so much :) 😝	train	1
147	go give ur mom a hug right now.	train	1
148	oh thank you!	train	1
149	pleased	train	1
150	Lmao.	train	1
151	Yep. I really love the couch for real	train	1
152	HA HA HA HA!!!!!	train	1
153	who else is in a happy mood?? =D	train	1
154	SO FAR SO GOOD!	train	1
155	TODAY WAS A GREAT DAY!!!	train	1
156	praise God for this beautiful day!!!	train	1
157	A blessed sunday everyone!	train	1
158	Just another day in paradise. ;)	train	1
159	All the small things...	train	1
160	My mom is the funniest person ever!	train	1
161	You aint gotta apologize. I know I'm not ugly.	train	1
162	I love to smile and have fun in life. I think that anyone and anything can be forgiven and we should all just love and be.	train	1
163	speak things into existence	train	1
164	If you see me smiling in public it means Im laughing at the jokes I tell myself in my head	train	1
165	in freshman year, it took me an hour and a half to get ready in the morning & now it takes me 6 minutes. now thats what i call improvement	train	1
166	I'M LAUGHING SO HARD AT THIS	train	1
167	This is the best public restroom Ive ever seen, every womens restroom should be like this	train	1
168	The best relationships to be in are the ones where you don't have to try hard because everything just flows naturally.	train	1
169	I think cuddling is one of the best feelings ever.	train	1
170	Breakfast in bed will be wonderful.	train	1
171	Thank you for making LOTB top 5 on the #Hot100 this week!  Glory to God	train	1
172	See y'all tomorrow.. rolling through PaRIH with my @puma crew at 9pm paris time. Get ready!	train	1
173	LOTB just became my 30th top ten hit on @billboard's Hot 100!!! Feeling so blessed  thank you Navy!!	train	1
174	Today's lit af! Played soccer on a dirt field with the most beautiful kids in Mchingi, Northern Malawi	train	1
175	THANK U from the bottom of my heart!	train	1
176	This made me so happy!! Check out what Vogue had to say about #FENTYxPUMA SS17	train	1
177	@CherrelleSkeete You're doing something beautiful. Block the bastards, then sing your heart out	train	1
178	Happy #MothersDay to mums everywhere & a special hug to all the people missing theirs today. Here's mine, Anne, with my little sis and me	train	1
179	Happy Birthday Lee. There will never be another like you. I'll cherish your passion & creativity 4ever. Unique doesn't begin to describe u	train	1
180	Love is knowing you were born this way! Support @BTWFoundation and help share kindness & compassion at http://theloveproject2017.com  #lovein3words	train	1
181	Monsters, let's show the world what love means to us. #lovein3words #theloveproject2017	train	1
182	Look who has a spring in their step! Celebrate the #FirstDayOfSpring by grabbing a friend, heading outside, and getting moving.	train	1
183	So impressed by the extraordinary girls I met at @CardozoEC who represent the beauty and diversity of this country. #InternationalWomensDay	train	1
184	I was thrilled to meet the young chefs from @MasterChefJrFOX last year! Tune in tonight to see what they cooked up. #MasterChefJunior	train	1
185	Thanks @chancetherapper for giving back to the Chicago community, which gave us so much. You are an example of the power of arts education.	train	1
186	Always love visiting DC schools. Thank you for hosting me today @BallouSTAY. Stories of students #reachinghigher continue to inspire me.	train	1
187	Remembering those who have made possible the dreams of today. Will never forget. Will never stop honoring their legacy. #BlackHistoryMonth	train	1
188	Happy Valentine's Day to the love of my life and favorite island mate, @BarackObama. #valentines	train	1
189	After an extraordinary 8 years, I'll be taking a little break. Will be back before you know it to work with you on the issues we care about.	train	1
190	Happy birthday, @MichelleObama!	train	1
191	On International Women’s Day, @MichelleObama and I are inspired by all of you who embrace your power to drive change.	train	1
192	I read letters like these every single day. It was one of the best parts of the job – hearing from you.	train	1
193	More than anything, I want to thank you all for everything. I am so grateful to every one of you for your support and your prayers.	train	1
194	Honored to narrate this video from @ET_AIDS_FDN highlighting the powerful activism of my hero, @ElizabethTaylor! #ETAF	train	1
195	Happy new yearzzzzz from me and my mama!!!! @tishcyrus	train	1
196	Miss you already! Thank you for your radical activism in the LGBTQ community! Love you always! @happyhippiefdn	train	1
197	One big happy @NBCTheVoice family! @aliciakeys @adamlevine @blakeshelton ! Can't wait to be back for season 13!!!!...https://instagram.com/p/BOBDJ_YBFvR/ 	train	1
198	We won each others Hearts!  Cheers to what's NEXT! #TeamMiley FOE EVA!! @MileyCyrus	train	1
199	So happy to be reunited with my flowaaaa child @DarbyAnneWalker	train	1
200	finally met my match! somebody who sticks their tongue out as much as me! #OGTongue !!!! fuck yeah Kiss! So bad ass tonight!	train	1
201	BFFs!!!!!! Best night ever! Celebrating Team Miley! @iamAliCaldwell @aarondgibson	train	1
202	Honored to be your coach & Lucky to call you my friend! Rock on Rocketman!   @aarondgibson	train	1
203	I love u my angel! I am so honored to be Ali's coach! Thank you for truly recognizing the star she is! Shinnnne @iamAliCaldwell	train	1
204	Vote for @aarondgibson now! Voting is open til 12pm ET/9am PT tomorrow! #VoiceTop8 #TeamMiley http://bit.ly/TheVoiceAPP 	train	1
205	Hey World, It's B! I'm so excited to invite you to my new http://beyonce.com  - we've been working hard, and it's finally ready for you XO	train	1
206	the work of dreams being studied with toni morrison. and junot diaz. for high school lit class. in brooklyn. ny.	train	1
207	love. also requires love.	train	1
208	Can't wait for #ElClasicoMiami at @HardRockStadium! @RealMadrid vs. @FCBarcelona!	train	1
209	So proud of my Girl @meghanmarkle writing this inspiring piece. You continue to inspire me everyday. Check it out: #	train	1
210	And also what are your recipes? I want to make some good shakes!!	train	1
211	Ummm words can't describe my excitement! Thank you @Starburst	train	1
212	San Jose, i love you! Thank you so much for your lovinnnn tonight. You have no idea how much joy…	train	1
213	I love you	train	1
214	One day I dream we'll do a whole project together and it'll be so tight. Love you forever, JRB.… https://www.instagram.com/p/BRr3V_wFe67/ 	train	1
215	Just saw the movie The Shack with the fam! Was so good to see after reading the book.	train	1
216	Had an amazing time celebrating my birthday. Thank you @Skylanders for making me feel like a kid again. #SkylandersAmbassador	train	1
217	Nothing like the raw energy of dancers in the studio! So beautiful and inspiring to watch! Obsessed!!!!	train	1
218	We are all in this together, as one, united in love. xo	train	1
219	GIRL POWER! So proud of @xtina and @alisanporter. #AlisanIsTheVoice	train	1
220	Kick off your shoes and dance? Done! Hanx	train	1
221	Thank you @tylerthecreator for being everything we dreamt of when making In Search Of. Artistic freedom to be you and make whatever you want	train	1
222	Amazing show. Rockets with @CHANEL on them. #HiddenFigures the movie comes out this week in Paris. Thank you Karl	train	1
223	new video is up babes! youtube bae @IngridNilsen stopped by to chat with me about lots of lovely LESBIAN STUFF	train	1
224	happy #iwd2017, ladybugs. gentle reminder that you are good enough. your strength is real. our humanity matters. keep going!	train	1
225	Justice is what LOVE looks like in public.	train	1
226	Amazing ! Thank you so much :)	train	1
227	Hope everyone has a lovely night tonight ! Thank you to absolutely every person that has been there for me and supported me this year !	train	1
228	Thank you for all the birthday message you're all lovely ! Had a big night last night so feeling it today 🍻 😷	train	1
229	Feeling so much love around me and my family . Mum would have been so fucking proud ( sorry for swearing mum 😝 ) love you !	train	1
230	All the support has been incredible! Let's do this together tonight .	train	1
231	Feeling super proud @NiallOfficial . You sound great ! Great to see you at your bday bash!!	train	1
232	Always soooooo nice to be back in England .. How I've missed you !	train	1
233	Time to change my number .. Getting some disgusting stuff on what's app... Losers !	train	1
234	Read so many amazing tweets from you guys ! Thanks for sharing the memories with us .. Here's to many more 🍻	train	1
235	Just seen all tweets .. You guys are incredible! Thanks for always making us smile 🙃	train	1
236	It's my friend Meg's 21st tomorrow and all she wants for her birthday is to raise money to help others !!! ... http://tmi.me/1fcFOM 	train	1
237	Incredible night . Thank you so much for making it so special !	train	1
238	Big love ! Have a good day everyone 🙃	train	1
239	Was great to start writing again yesterday! 😎	train	1
240	My second family	train	1
241	last night ❤	train	1
242	Nothing like a full bar singing along to Queen to turn a bad mood around #winning	train	1
243	Falling in love with @Brodinski Intense dance music that you want to listen to again n again. Gimme Back the Night!	train	1
244	OMG OMG OMG OMG!!!	train	1
245	You know how you're running and you get into the flow, and forget you're running and it's just you and your thoughts. What a feeling!!	train	1
246	I learned, I laughed, I cried. Oh man, this is fantastic.	train	1
247	is so sad for my APL friend.............	train	2
248	I missed the New Moon trailer...	train	2
249	or i just worry too much?   	train	2
250	 this weekend has sucked so far	train	2
251	Very sad about Iran.	train	2
252	Boring ): what's wrong with him?  Please tell me.	train	2
253	I miss Earl	train	2
254	I miss New Jersey	train	2
255	I missed the first hour of SYTYCD last night, and I can't find it online!	train	2
256	I need a U2 fix NOW!	train	2
257	I never thought I'd become second choice...	train	2
259	I wanted to sleep in this morning but a mean kid threw a popsicle stick at me head. I wish I could fly away like those squirrels	train	2
260	My new car was stolen....by my mother who wanted to go pose at church.	train	2
261	Ugh it's a parody account. I have been tricked too many times today.	train	2
262	Oh man do I have a tummy bug from hell. Why do I always order the riskiest shit on the plane like hell yeah plane clams sound great gimme	train	2
263	missing my friends!	train	2
264	Missing my friends!!	train	2
265	Missing my fiancee sooo badly!!! I love you baybay!	train	2
266	Missing my family lots tonight	train	2
267	Missing my family in the USA	train	2
268	missing my daily dose of Scrabble on Facebook	train	2
269	Missing my daddy this weekend I still miss him each and every day..	train	2
270	Missin my baby apple I hope everything is ok	train	2
271	missin my baby girl	train	2
272	Missin my baby stephen	train	2
273	missin' my baby...	train	2
274	Missin my baby....	train	2
275	Missin' my BFF	train	2
276	MiSsIn My bOo	train	2
277	missin' my boyfriend...	train	2
278	Missin my bubba	train	2
279	Missin my baby apple I hope everything is ok	train	2
280	missin my baby girl	train	2
281	Missin my baby stephen	train	2
282	missin' my baby...	train	2
283	Missin my baby....	train	2
284	Missin' my BFF	train	2
285	MiSsIn My bOo	train	2
286	missin' my boyfriend...	train	2
287	Missin my bubba	train	2
288	misses his phone more than life	train	2
289	Misses his sork	train	2
290	misses home on the farm	train	2
291	misses home-made sandwiches already...	train	2
292	Misses ihearteggrollzz and spriteluver wishes I was with then. And I turned friggin dark!!!!	train	2
293	misses iKRMZ, ACS and ALL very much. ...Hmm..I wonder...	train	2
294	misses Jarred. Doing work for last day of class/studio time tomorrow at the New School!	train	2
295	misses JMU/Spotswood &lt;3	train	2
296	misses Jon already	train	2
297	misses Joy, Renz, Serge, Renzo, Ken and Arvin! Good thing i see Maan and Pria everyday (lol) http://plurk.com/p/11kjfy	train	2
298	Misses JP I do not know what to do and iv given myself a headache thinking about it, just makes me want to cry	train	2
299	misses kdh.. So much!!! Cant sleep w/o his voice	train	2
300	misses lance already...	train	2
301	Misses Leno...Conan sucks monkey butts.	train	2
302	misses lillian	train	2
303	misses living with @MegUp .... back to orientation tommorow morning	train	2
304	misses Liz's awesomeness	train	2
305	misses loulou so bad	train	2
306	misses Mark already Getting sick sucks donkey balls	train	2
307	Misses matty poo! he'll get a dutch rudder when he gets back! Lmao	train	2
308	misses Max. RIP I miss you little dude.	train	2
309	misses mendy already!!!	train	2
310	misses mom already.	train	2
311	Misses Mr.Pepper	train	2
312	misses my andy..	train	2
313	Misses my baby bunny penny	train	2
314	misses my best friend...it sucks when good ppl r only in ur life for a season...	train	2
315	misses my Boyfriend	train	2
316	misses my mom	train	2
317	misses my Mosaic fam.	train	2
318	misses my pothole republic	train	2
319	misses my sister @rashandamccants and my brother @rashadmccants7	train	2
320	misses nicholas so much. I need a a forehead kiss!	train	2
321	misses playing board games	train	2
322	misses playing don't you dare during class.	train	2
323	misses playing music!	train	2
324	Misses Rach already	train	2
325	misses Rob something cronic, and he only left two mins ago ....	train	2
326	Misses sara already no one to talk to	train	2
327	misses school already	train	2
328	Misses seb long time	train	2
329	Misses Sheetz and all the places I was at this past weekend	train	2
330	misses Silver..	train	2
331	misses sleeping with g.babe	train	2
332	misses someone	train	2
333	misses someone so bad right now.	train	2
334	misses someone verymuchalot right now.	train	2
335	misses Sue and she's only just gone to work. Her working nighs sucks!	train	2
336	Misses summer.	train	2
337	misses surfing!	train	2
338	misses talking on the radio. I was listening to my old radio shows today and almost shedded a tear. I need to get back on the airwaves!!	train	2
339	misses talking to Mugen. Well, and Jin. She wants to talk to either one of them, really...	train	2
340	misses the boy thhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiissssssssssssssssssssssss much	train	2
341	Misses the cutest boy eveer wonder if hes thinking about me as much as im thinking about him?	train	2
342	Misses the electric guitar	train	2
343	misses the f*$k out of him and cant believe how bloody cru el he can be	train	2
344	misses the first dumbledore	train	2
345	misses the getaway boys already	train	2
346	Misses the life of being a dancer, taking 5-6 hours of dance a day, rehearsing and performing ballet	train	2
347	misses the movie The little vampire used to love it wen i was little	train	2
348	misses the States already.	train	2
349	Misses the sunshine	train	2
350	Misses the Turk team	train	2
352	misses tivo had to watch desperate housewives online	train	2
353	Misses Tricia and Bernadette	train	2
354	misses watching Entourage	train	2
355	trump furiously trying to ban television right now	train	2
356	Some people are just hell bent on being the fucking worst.	train	2
357	Imagine being this miserable. We are fine, thanks.	train	2
358	Every god damn person on this plane has peed I've never seen anything like it	train	2
359	i lost myself in the process of loving someone that i thought will be with me forever.	train	2
360	nothing hurts more than haven your heart broken by the one person that you thought would of never hurt you.	train	2
361	nothing hurts more than knowing that doing your best wasn't good enough for someone.	train	2
362	Disgusted! The news is devastating! America is being ruined right before our eyes! What an immoral pig you have to be to implement such BS!!	train	2
363	My heart goes out to the victims and their families in London. No act of terror can shake the strength and resilience of our British ally.	train	2
364	My prayers are with everyone affected by last night’s senseless tragedy. We can’t tolerate hate. Don’t lose hope, we can #change the future.	train	2
365	The Age of Trump is an age of spiritual blackout.	train	2
366	#BlackWomenAtWork dedicated, overworked, unappreciated, stressed, and called the angry black woman when we reach our breaking points.	train	2
367	In contrast, Corbyn totally misjudging the mood, (as always). Doing his angry, ranty routine.	train	2
368	#BlackWomenAtWork silencing my emotions for fear of being labeled as either "angry" or "unstable".	train	2
369	this is sad to think but i think theyre gonna practice more & less rest and minhyuk is sick but he probs gonna force himself to practice :(	train	2
370	Just chopped up my Lib Dem membership card with toenail clippers in protest at @timfarron's PATHETIC lack of opposition to Brexit. Sad!	train	2
371	A sad day for democracy in Spain. @franceschoms forced to step down as MP. Banned from office in political trial for his pro-indy actions.	train	2
372	Not a day goes by without Trump playing the victim card. Who hurt him. What "they" said about him. What a sad little man.	train	2
373	i'm either sad, tired, annoyed or all three	train	2
374	Such a sad, disappointing, horrible day - #brexitday is here 😢😔 #NotInMyName ️✌🏼️	train	2
375	i don't like seeing my friends sad, tara hug ko kayo ☹️	train	2
376	Outside: Smiling. Okay. Happy. Inside: Broken. Crying. Sad.	train	2
377	hobbies include: irrational fear of small talk, holding a grudge against my parents for making me exist	train	2
378	i'm still in love with who you used to be.	train	2
379	it's sad because everyone turns out exactly how they promised they never would	train	2
380	crazy how someone can ruin an amazing day with a few simple actions	train	2
381	whats the point of having so many friends but when you're at your lowest point, not even one of them is there for you	train	2
382	please be careful	train	2
383	Lowkey wanna be a sweetheart but everyone annoys me	train	2
384	do u ever miss yourself, like your former self like maybe you used really passionate abt something and yr not anymore and ..u just miss it	train	2
385	me at 2 am tweeting to only myself about how sad I am	train	2
386	Sometimes timing just doesn't work in your favor.. no matter how much you want that person	train	2
387	IF U ABUSE AN ANIMAL U DESERVE TO BE BURIED ALIVE, THEY DONT EVEN UNDERSTAND WHATS HAPPENING ALL THEY TRY TO DO IS MAKE U HAPPY	train	2
388	you were a dream, then a reality and now just a memory.	train	2
389	when you can't find anything to wear so you have a 10 minute breakdown instead of getting ready	train	2
390	My prayers are with the families who lost loved ones tonight. This is not humanity. Just chaos.	train	2
391	This is ridiculous. Why do I keep having to ask myself what century it is??	train	2
392	Trump is a lying, indecent man who has offended so many people in this country & around the world -except Putin. He doesn't belong in the WH	train	2
393	Disappointed in @Dropbox for putting profit ahead of customer service and charging for licenses you don't need @drewhouston @DropboxSupport	train	2
394	So disappointed @JetBlue for adding a checked bag fee. @SouthwestAir, can you add direct flights from SF to Boston, please.	train	2
395	The very best way to support and feed your delusions: Surround yourself with people whose world views match yours exactly.	train	2
396	Very disheartened w/confirmation of @BetsyDeVos & #JeffSessions Traveling for work & catching up on the news. Lots of work to do America.	train	2
397	He was murdered in a hate crime, by a man shouting "get out of my country". Srinivas Kuchibhotla was 32 years old. Why is this ignored?	train	2
398	The murder of Srivinas Kuchibhotla is incomprehensible. The anguish of his family. This must continue to shock us, it cannot be normalized.	train	2
399	This is gross.	train	2
400	I don't feel good	train	2
401	My mom just said her back hurts when she's not pooping	train	2
402	I feel like pure garbage. SOBER AND HEALTHY WEEK STARTS NOW (I feel like if I tweet this, I'll actually stick to it) I smell like hot dogs	train	2
403	I'm so sorry to hear that someone got hurt at my show tonight. It's being investigated to ensure it won't happen again. X	train	2
404	The piano mics fell on to the piano strings, that's what the guitar sound was. It made it sound out of tune. Shit happens. X	train	2
405	Devastated to hear about Bill. A privilege to have worked with him. What a huge-hearted man. All my love to his family.	train	2
406	Why are all my friends/ex so lame and won't do fear factor with me?	train	2
407	Gotta be honest. I'm hoping the leaked @VansWarpedTour lineup is not real. I'd be a little disappointed.	train	2
408	I have exactly 53 minutes to turn in an assignment that I haven't even looked at. #college	train	2
409	I'd suggest not talking to me right now in case anyone was going to.	train	2
410	If you're trying to start a snap streak with me you better be committed because I'm about to be pissed if we lose it.	train	2
411	I honestly wish you were a better person.	train	2
412	So there's this boy and I sorta kinda of love him but I don't think he feel the same 🤦🏽‍♀️	train	2
413	I'm not finna beg anymore  if you want to leave I don't care no mo ,you can bounce .....	train	2
414	Damn Really thought it would be my year 😭	train	2
415	I hate the fact that one bad thing can happen and it can ruin a beautiful relationship  🤦🏽‍♀️ 👎🏾 🙄	train	2
416	I'm tired of fake people, fake smiles, fake hugs, fake hope, fake friends, fake love.	train	2
417	She claimed she was my sister but she really a snake smh 🤦🏽‍♀️	train	2
418	The privacy laws are fucked up 😡	train	2
419	House about to burn down and we are all snapping it like morons	train	2
420	My nail broke. And it's still fucking green	train	2
421	Arrrrrgh I hate the hollywoods peoples I'm on twitter with followers arghhhhh rarrrrrrr	train	2
422	i should have known telling you guys anything would lead to two million people telling me how to live but that's my own damn fault	train	2
423	Donald Trump is an unwell, evil human being. To the core.	train	2
424	I do not physically have the energy for this presidency to lie every single fucking day. Please. Just bring it down to every other day.	train	2
425	People in pain. People need jobs. People need healthcare. People want equality. But let's have a press conference on crowd size. My god.	train	2
426	I have not put my phone down once today. My hand, it aches. My eyes, dry. My pettiness...my pettiness has somehow maintained its strength	train	2
427	You gotta be kidding me	train	2
428	I was very kind. Answered cooking questions, then he came with that. Fucking disgusting.	train	2
429	i ripped two of my nails off in the dresser drawer and cannot touch anything without slightly sobbing	train	2
430	i am 31 years old and have never done yoga. how stupid will i look in a class? i feel like everyone in a class has done it before :(	train	2
431	I am so hungover that each individual tooth hurts in a different way	train	2
432	She legit stole the car of a producer working on her episode and came back a day later having stolen her money. A ranch not gonna help, man	train	2
433	I dunno I just don't trust that Burlington has coats anymore	train	2
434	Who can protect us from our own president-elect???? We need a president of the world or something. Universe. Someone. Please help us.	train	2
435	Who is gonna tell them, I don't have the heart 	train	2
436	smoking my turkey for the first time this year. frying sucks, roasting sucks, turkey sucks. this better not suck.	train	2
437	My daughter isn't on social media, you ignorant tool. Go fuck yourself. Fuck fuck fuck!	train	2
438	I'll never understand this mentality. That only certain people are allowed to speak? Who are the people allowed to speak, Cindy? 	train	2
439	Interested to see if trump supporters will be able to criticize the inevitable dumpster fire that will ultimately be his actual presidency	train	2
440	Look who wants a fucking safe space now. The very thing him and his supporters make fun of as liberal political correctness. God, what a POS	train	2
441	You don't get to sue a company because a rat part was sewn into your jacket. There is no jacket distress. Return your rat jacket.	train	2
442	America is in a Russian-hacking led dumpster fire but okay. Let's talk plates.	train	2
443	So fucking sick of racist, sexist, homophobic bullshit. Always been sick of it but now I'm gonna fucking swear about it. Try and stop me!	train	2
444	Bill O'Reilly is straight up trash. I'm sick of this BS. Dude has settled multiple sexual harassment lawsuits. Ailes is gone,O'Reilly stays?	train	2
445	Omg get over it!!!	train	2
446	This Ish is crazy!!!!!!! How ITF do they get away with this	train	2
\.


--
-- Name: classifier_classifier_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('classifier_classifier_id_seq', 446, true);


--
-- Data for Name: quotes; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY quotes (quote_id, content, img_url, author, sentiment_id) FROM stdin;
1	Aerodynamically, the bumble bee shouldn't be able to fly, but the bumble bee doesn't know that so it goes flying anyway.	static/poem_image/bee.jpg	Mary Kay Ash	1
2	When a flower doesn't bloom, you fix the environment in which it grows, not the flower.	static/poem_image/bloom.jpg	Alexander Den Heijer	1
3	Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself.	static/poem_image/clever.jpg	Rumi	1
4	I want to stay as close to the edge as I can without going over. Out on the edge you see all kinds of things you can't see from the center.	static/poem_image/edge.jpg	Kurt Vonnegut	1
5	Flawesome - (adj.) An individual who embraces their "flaws" and knows they're awesome regardless.	static/poem_image/flawsome.jpg	NULL	1
6	The best part about heroes is sometimes you get to be your own.	static/poem_image/heroes.png	Cleo Wade	1
7	You cannot get through a single day without having an impact on the world around you. What you do makes a difference, and you have to decide what kind of difference you want to make.	static/poem_image/impact.jpg	Jane Goodall	1
8	Be kind to unkind people. They need it most.	static/poem_image/kind.jpg	NULL	1
9	In a society that profits from your self doubt, liking yourself is a rebellious act.	static/poem_image/liking_yourself.jpg	unknown	1
10	Why not go out on a limb? That's where all the fruit is.	static/poem_image/limb.jpg	Mark Twain	1
11	how you love yourself is how you teach others to love you	static/poem_image/love_yourself.png	Rupi Kaur	1
12	Be the love you never received.	static/poem_image/received.jpg	Rune Lazuli	1
13	People who wonder whether the glass is half empty or half full miss the point... The glass is refillable.	static/poem_image/refillable.jpg	NULL	1
14	i love myself.' the quietest. simplest. most powerful. revolution. ever.	static/poem_image/revolution.jpg	Nayyirah Waheed	1
15	My alone feels so good. I'll only have you if you're sweeter than my solitude.	static/poem_image/solitude.png	Warsan Shire	1
16	To my children: Never make fun of having to help me with computer stuff. I taught you how to use a spoon.	static/poem_image/spoon.png	NULL	1
17	Make time for yourself. You are important.	static/poem_image/time.jpg	NULL	1
18	when I look at myself in the mirror. i see a unicorn. a badass unicorn.	static/poem_image/unicorn.jpg	unknown	1
19	Sometimes you want to be a princess and Darth Vader...at the same time.	static/poem_image/vaderprincess.jpg	unknown	1
20	Being a little weird is just a natural side-effect of being awesome.	static/poem_image/weird.jpg	Sue Fitzmaurice	1
21	You not wanting me was the beginning of me wanting myself. Thank you.	static/poem_image/you_not_wanting_me.png	Nayyirah Waheed	1
22	Be yourself. Everyone else is already taken.	static/poem_image/yourself.jpg	Oscar Wilde	1
23	We are all a little weird and life's a little weird. And when we find someone whose weirdness is compatible with ours, we join up with them and fall in mutual weirdness and call it love.	static/poem_image/mutual_weirdness.jpg	Dr. Seusss	1
24	Always forgive your enemies, nothing annoys them so much.	static/poem_image/forgive.jpeg	Oscar Wilde	1
25	Life is too important to be taken seriously!	static/poem_image/seriously.jpg	Oscar Wilde	1
26	In your soul are infinitely precious things that cannot be taken from you.	static/poem_image/infinitely.jpg	Oscar Wilde	1
27	The Mad Hatter: 'Have I gone mad?' Alice: 'I'm afraid so. You're entirely bonkers. But I'll tell you a secret. All the best people are.'	static/poem_image/bonkers.jpg	Lewis Carroll	1
28	If ever there is tomorrow when we're not together... there is something you must always remember. You are braver than you believe, stronger than you seem, and smarter than you think. But the most important thing is, even if we're apart... I'll always be with you.	static/poem_image/tomorrow.jpg	A. A. Milne	1
29	If speaking kindly to plants helps them grow imagine what speaking kindly to humans can do.	static/poem_image/plants.jpg	NULL	1
30	you can not remain a war between what you want to say (who you really are). and what you should say (who you pretend to be). your mouth was not designed to eat itself. -split	static/poem_image/at_war.jpg	Nayyirah Waheed	2
31	The most beautiful people we have known are those who have known defeat, known suffering, known struggle, known loss, and have found their way out of the depths. These persons have an appreciation, a sensitivity, and an understanding of life that fills them with compassion, gentleness, and a deep loving concern. Beautiful people do not just happen.	static/poem_image/beautiful_people.jpg	Elisabeth Kubler-Ross	2
32	And I said to my body. softly. 'I want to be your friend.' It took a long breath. And replied, 'I have been waiting my whole life for this.'	static/poem_image/body.jpg	Nayyirah Waheed	2
33	Be careful how you talk to yourself, because you are listening.	static/poem_image/careful.jpg	NULL	2
34	My last day of chemo. It was tough, but I was tougher.	static/poem_image/chemo.jpeg	NULL	2
35	where you are. is not who you are.  -circumstances	static/poem_image/circumstances.jpg	Nayyirah Waheed	2
36	I did not come this far to only come this far.	static/poem_image/come.png	NULL	2
37	be easy. take your time. you are coming home. to yourself.	static/poem_image/coming_home.jpg	Nayyirah Waheed	2
38	deep down in your cells. you know the truth. you are exquisite. and yes. you are that powerful. and it scares you.	static/poem_image/deep_down.jpg	Nayyirah Waheed	2
39	you deserve the love you keep trying to give everyone else	static/poem_image/deserve.jpg	NULL	2
40	I've never met a strong person with an easy past.	static/poem_image/easy_past.jpg	unknown	2
41	Talent is insignificant. I know a lot of talented ruins. Beyond talent lie all the usual words: discipline, love, luck, but, most of all, endurance.	static/poem_image/endurance.jpg	James Baldwin	2
42	you are enough	static/poem_image/enough.png	NULL	2
43	fall apart. please just, fall apart. open your mouth. and hurt. hurt the size of everything it is. -dam	static/poem_image/fall_apart.jpg	Nayyirah Waheed	2
44	Before you diagnose yourself with depression or low self-esteem, first make sure you are not, in fact, surrounded by assholes.	static/poem_image/freud.jpg	Sigmund Freud	2
45	In Japan, broken object are often repaired with gold. The flaw is seen as a unique piece of the object's history, which adds to its beauty. Consider this when you feel broken.	static/poem_image/gold.jpg	NULL	2
46	We are all in the gutter, but some of us are looking at the stars.	static/poem_image/gutter.jpg	Oscar Wilde	2
47	in our own ways we all break. it is okay to hold your heary outside of your body for days. months. years. at a time.	static/poem_image/heal.jpg	Nayyirah Waheed	2
48	Between what is said and not meant, and what is meant and not said, most of love is lost.	static/poem_image/love_lost.jpg	Khalil Gibran	2
49	i am trying to remember you and let you go at the same time	static/poem_image/mourn.jpg	Nayyirah Waheed	2
50	Healing is not linear.	static/poem_image/not_linear.jpg	NULL	2
51	Holding onto anger is like drinking poison and expecting the other person to die.	static/poem_image/poison.jpg	Buddha	2
52	As I look back on my life, I realize that every time I thought I was being rejected from something good, I was actually being re-directed to something better.	static/poem_image/rejected.jpg	NULL	2
53	Caring for myself is not self-indulgence, it is self-preservation and that is an at of poltiical warfare.	static/poem_image/self_preservation.jpg	Audre Lorde	2
54	Be messy and complicated and afraid and show up anyways.	static/poem_image/show_up.png	Glennon Doyle Melton	2
55	You are enough. You are so enough. It is unbelievable how enough you are.	static/poem_image/so_enough.png	NULL	2
56	People always think that the most painful thing in life is losing the one you value. The truth is, the most painful thing is losing yourself in the process of valuing someone too much and forgetting that you are special too.	static/poem_image/special.jpg	NULL	2
57	Failure is a bruise. Not a tattoo.	static/poem_image/tattoo.jpg	Jon Sinclair	2
58	You are allowed to terminate toxic relationships. You are allowed to walk away from people who hurt you. You don't owe anyone an explanation for taking care of yourself.	static/poem_image/toxic.jpg	NULL	2
59	i found flaws and they were beautiful. -ugly	static/poem_image/ugly.jpg	Nayyirah Waheed	2
60	you will be lost and unlost. over and over again. relax love. you were meant to be this glorious. epic. story.	static/poem_image/unlost.jpg	Nayyirah Waheed	2
61	So far you've survived 100% of your worst days. You're doing great!	static/poem_image/worst_days.jpg	NULL	2
62	The wound is the place where the light enters you.	static/poem_image/wound.jpg	Rumi	2
63	Your value does not decrease based on someone's inability to see your worth.	static/poem_image/your_value.png	unknown	2
64	The world is a stage, but the play is badly cast.	static/poem_image/cast.png	Oscar Wilde	2
65	like wildflowers; you must allow yourself to grow in all the places people thought you never would.	static/poem_image/wildflowers.jpg	E.V.	2
66	Choose, everyday to forgive yourself. You are human, flawed, and most of all worthy of love.	static/poem_image/choose.jpg	Alison Malee	2
67	No.	static/poem_image/no.png	Rosa Parks	2
68	Rome is built on ruins And is quite breathtaking; What makes you think You can't be too?	static/poem_image/rome.jpg	Anon	2
69	The cure for anything is saltwater---sweat, tears, or the sea.	static/poem_image/saltwater.jpg	Isak Dinesen	2
70	do not look for healing at the feet of those who broke you	static/poem_image/feet.jpg	Rupi Kaur	2
237	I am a positive quote!	static/positivequote.jpg	me	1
238	I am a negative quote!	static/negativequote.jpg	you	2
239	I am a positive quote!	static/positivequote.jpg	me	1
240	I am a negative quote!	static/negativequote.jpg	you	2
\.


--
-- Name: quotes_quote_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('quotes_quote_id_seq', 240, true);


--
-- Data for Name: sentiments; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY sentiments (sentiment_id, sentiment) FROM stdin;
1	pos
2	neg
\.


--
-- Name: sentiments_sentiment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('sentiments_sentiment_id_seq', 186, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY users (user_id, user_name, password, twitter_handle, email, phone, reminder_time) FROM stdin;
2	katie	hello	katiet	katie@taylor.com	5553338888	\N
255	Favinn	clown eyes	NuBaby	Favinn@gmail.com	555-444-9999	evening
256	Aimee	art	Artist	Aimee@gmail.com	555-555-9999	morning
1	hannah	password	HannahSchafer18	hannah@banana.com	610-742-1594	morning and evening
257	Charlotte	house	RedHead	Charlotte@gmail.com	333-555-9999	evening
258	Favinn	clown eyes	NuBaby	Favinn@gmail.com	555-444-9999	evening
259	Aimee	art	Artist	Aimee@gmail.com	555-555-9999	morning
260	Charlotte	house	RedHead	Charlotte@gmail.com	333-555-9999	evening
261	Dan	pw	danpal	dan@dan.com	555-555-3344	\N
3	Aurora	aurora	AuroraTallin25	AuroraTallin25@gmail.com	222-222-2222	evening
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('users_user_id_seq', 261, true);


--
-- Name: analyses_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY analyses
    ADD CONSTRAINT analyses_pkey PRIMARY KEY (analyses_id);


--
-- Name: classifier_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY classifier
    ADD CONSTRAINT classifier_pkey PRIMARY KEY (classifier_id);


--
-- Name: quotes_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY quotes
    ADD CONSTRAINT quotes_pkey PRIMARY KEY (quote_id);


--
-- Name: sentiments_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY sentiments
    ADD CONSTRAINT sentiments_pkey PRIMARY KEY (sentiment_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: analyses_quote_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY analyses
    ADD CONSTRAINT analyses_quote_id_fkey FOREIGN KEY (quote_id) REFERENCES quotes(quote_id);


--
-- Name: analyses_tweet_sent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY analyses
    ADD CONSTRAINT analyses_tweet_sent_id_fkey FOREIGN KEY (tweet_sent_id) REFERENCES sentiments(sentiment_id);


--
-- Name: analyses_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY analyses
    ADD CONSTRAINT analyses_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: classifier_sentiment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY classifier
    ADD CONSTRAINT classifier_sentiment_id_fkey FOREIGN KEY (sentiment_id) REFERENCES sentiments(sentiment_id);


--
-- Name: quotes_sentiment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY quotes
    ADD CONSTRAINT quotes_sentiment_id_fkey FOREIGN KEY (sentiment_id) REFERENCES sentiments(sentiment_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


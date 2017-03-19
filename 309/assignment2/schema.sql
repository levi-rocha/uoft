create table twocuser (username varchar(20) primary key, password varchar(999). picture varchar(999));

create table post (id serial primary key, username varchar(20) references twocuser (username), picture varchar(999), content varchar(9999), likes integer, timestamp timestamp default current_timestamp);

insert into twocuser values ('developer', 'f5d1278e8109edd94e1e4197e04873b9', 'img/me.jpg');

insert into twocuser values ('pikachu', 'edb6eb67ad923f497521c09cab18e82c', 'img/pikapika.jpg');

insert into post (username, picture, content, likes) values ('developer', 'img/me.jpg', <p></p><span style="font-size:20px;">20</span><span style="font-size:42px;">caught</span><span style="font-size:20px;">some</span><span style="font-size:36px;">pokemon</span><span style="font-size:36px;">@pokemon:</span><span style="font-size:20px;">happy</span><span style="font-size:28px;">pokémon</span><span style="font-size:20px;">day!</span><span style="font-size:20px;">years</span><span style="font-size:20px;">#pokemon20!</span><span style="font-size:20px;">keep</span><span style="font-size:28px;">@pokemon</span><span style="font-size:20px;">looks</span><span style="font-size:20px;">throw</span><span style="font-size:20px;">another</span><span style="font-size:28px;">poké</span><span style="font-size:20px;">ball</span><span style="font-size:28px;">see</span><span style="font-size:20px;">else</span><span style="font-size:20px;">hiding</span><span style="font-size:20px;">tall</span><span style="font-size:20px;">grass!</span><span style="font-size:20px;">not</span><p></p>, 0);

insert into post (username, picture, content, likes) values ('pikachu', 'img/pikapika.jpg', <p></p><span style="font-size:20px;">need</span><span style="font-size:60px;">sleep</span><span style="font-size:20px;">night</span><span style="font-size:20px;">sleep.</span><span style="font-size:20px;">no</span><span style="font-size:20px;">@camerondallas:</span><span style="font-size:20px;">tight</span><span style="font-size:20px;">??</span><span style="font-size:20px;">not</span><span style="font-size:20px;">he</span><p></p>, 0);

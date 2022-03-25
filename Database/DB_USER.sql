CREATE DATABASE db_user;
use db_user;

CREATE TABLE tb_user(
    tb_user_id integer not null auto_increment primary key,
    tb_user_nome varchar(100) not null,
    tb_user_email varchar(100) not null,
    tb_user_pass varchar(100)not null,
    tb_user_sexo char(1)not null
);

select*from tb_user;
#SELECT tb_user_pass, tb_user_email FROM tb_user WHERE tb_user_email = "lovato.py@gmail.com" and ;
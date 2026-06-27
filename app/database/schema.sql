create extension if not exists pgcrypto;
create database if not exists MbPflegeRegistry;
use MbPflegeRegistry;

create table if not exists staff (
    staff_id serial primary key, 
    staff_fname varchar(20) not null, 
    staff_lname varchar(20) not null,
    staff_email varchar(50) unique not null,
    staff_password_hash text not null,
    staff_phone varchar(15),
    staff_address text not null,
    staff_street_name varchar(50) not null,
    staff_suburb varchar(50) not null,
    staff_city varchar(50) not null,
    staff_postal_code varchar(10) not null,
    staff_role varchar(20) not null, 
        -- 'admin', 'arzt', 'therapeut', 'pflegekraft', 'vermischt'
);

create table if not exists password_resets (
    email varchar(100) not null primary key, 
    token_hash varchar(100) not null, 
    token_expiration timestamp not null
);

create table if not exists patients (
    patient_id serial primary key,
    patient_fname varchar(20) not null, 
    patient_lname varchar(20) not null,
    patient_email varchar(50) unique not null,
    patient_phone varchar(15),
    patient_dob date not null,
    patient_gender varchar(10) not null,
    patient_address text not null, 
    patient_street_name varchar(50) not null,
    patient_suburb varchar(50) not null,
    patient_city varchar(50) not null,
    patient_postal_code varchar(10) not null,
);

create table if not exists medicine (
    medicine_id serial primary key,
    medicine_name varchar(50) not null,
    medicine_std_dosage varchar(20) not null,
    medicine_frequency varchar(20) not null,
    medicine_side_effects text, 
    medicine_stock not null int
);

create table if not exists medicine_logs (
    medicine_log_id serial primary key,
    staff_id int references staff(id),
    patient_id int references patients(id),
    medicine_id int references medicine(id),
    medicine_log_dosage varchar(20) not null,
    medicine_log_administration_time timestamp,
    medicine_log_notes text
);

create table if not exists schedules (
    schedules_id serial primary key,
    staff_id int references staff(id),
    patient_id int references patients(id),
    schedule_time timestamp,
    status text default 'planmäßig', 
        -- 'planmäßig', 'fertiggestellt', 'storniert', 'vermisst'
    notes text
);

create table if not exists audit_logs (
    audit_log_id serial primary key,
    staff_id int references staff(id),
    audit_ip_address inet,
    action varchar(50) not null,
    details text, --eg. patient_id, medicine_id, etc (was mochtet man zugriffen haben?)
    audit_timestamp timestamptz default now()
);

alter table staff add column reset_token_hash;
alter table staff add column reset_token_expires timestampz;
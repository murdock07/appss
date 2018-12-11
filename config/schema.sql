drop table if exists PlantInfos;
create table PlantInfos (
    PlatnId text,
    PlantName text,
    MinWaterLevel integer,
    MaxWaterLevel integer,
    MinLightLevel integer,
    MinLightInterval integer,
    MinTemperature integer,
    MaxTemperature integer,
    MinHumidity integer,
    MaxHumidity integer
);
INSERT INTO PlantInfos ();

drop table if exists Measurements;
create table Measurements (
    MeasureTime text,
    Sensor text,
    MeasuredValue real,
);

drop table if exists Logs;
create table Logs (
    Id integer,
    LogTime text,
    LogMessage text,
    LogSeverity text
);
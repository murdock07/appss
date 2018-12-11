drop table if exists PlantInfos;
create table PlantInfos (
    PlatnId integer,
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
INSERT INTO PlantInfos (PlatnId, PlantName, MinWaterLevel, MaxWaterLevel, 
                        MinLightLevel, MinLightInterval, MinTemperature,
                        MaxTemperature, MinHumidity, MaxHumidity)
            VALUES (1, "Chili", 8, 9, 7, 10, 22, 35, 2, 5);

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
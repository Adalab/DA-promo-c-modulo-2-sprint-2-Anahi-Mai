
import src.soporte as sp


iniciacion= sp.Subida_datos('tiburones', 'AlumnaAdalab')

print('Has iniciado la clase de "Subida_datos"')

iniciacion.crear_bbdd()

query_ataques= '''
CREATE TABLE IF NOT EXISTS `tiburones`.`ataques` (
`id_ataque` INT NOT NULL AUTO_INCREMENT,
`case_number` VARCHAR(45),
`year` FLOAT ,
`mes` VARCHAR(45),
`sexo` VARCHAR(45),
`edades` FLOAT,
`country` VARCHAR(45),
`type` VARCHAR(45),
`activity` VARCHAR(240), 
`fatal` VARCHAR(45), 
`cat_species` VARCHAR(45), 
PRIMARY KEY (`id_ataque`,`country`),
KEY idx_country (`country`))
ENGINE = InnoDB;
'''

query_clima= '''CREATE TABLE IF NOT EXISTS `tiburones`.`clima` (
`id_clima` INT NOT NULL AUTO_INCREMENT,
`country` VARCHAR(45) NOT NULL,
`speed950mb` FLOAT NOT NULL,
`speed900mb` FLOAT NOT NULL,
`speed850mb` FLOAT NOT NULL,
`speed800mb` FLOAT NOT NULL,
`speed750mb` FLOAT NOT NULL,
`speed700mb` FLOAT NOT NULL,
`speed650mb` FLOAT NOT NULL,
`speed600mb` FLOAT NOT NULL,
`speed550mb` FLOAT NOT NULL,
`speed500mb` FLOAT NOT NULL,
`speed450mb` FLOAT NOT NULL,
`speed400mb` FLOAT NOT NULL,
`speed350mb` FLOAT NOT NULL,
`speed300mb` FLOAT NOT NULL,
`speed250mb` FLOAT NOT NULL,
`speed200mb` FLOAT NOT NULL,
`direction200mb` FLOAT NOT NULL,
`direction250mb` FLOAT NOT NULL,
`direction300mb` FLOAT NOT NULL,
`direction350mb` FLOAT NOT NULL,
`direction400mb` FLOAT NOT NULL,
`direction450mb` FLOAT NOT NULL,
`direction500mb` FLOAT NOT NULL,
`direction550mb` FLOAT NOT NULL,
`direction600mb` FLOAT NOT NULL,
`direction650mb` FLOAT NOT NULL,
`direction700mb` FLOAT NOT NULL,
`direction750mb` FLOAT NOT NULL,
`direction800mb` FLOAT NOT NULL,
`direction850mb` FLOAT NOT NULL,
`direction900mb` FLOAT NOT NULL,
`direction950mb` FLOAT NOT NULL,
`rh_950mb` FLOAT NOT NULL,
`rh_900mb` FLOAT NOT NULL,
`rh_850mb` FLOAT NOT NULL,
`rh_800mb` FLOAT NOT NULL,
`rh_750mb` FLOAT NOT NULL,
`rh_700mb` FLOAT NOT NULL,
`rh_650mb` FLOAT NOT NULL,
`rh_600mb` FLOAT NOT NULL,
`rh_550mb` FLOAT NOT NULL,
`rh_500mb` FLOAT NOT NULL,
`rh_450mb` FLOAT NOT NULL,
`rh_400mb` FLOAT NOT NULL,
`rh_350mb` FLOAT NOT NULL,
`rh_300mb` FLOAT NOT NULL,
`rh_250mb` FLOAT NOT NULL,
`rh_200mb` FLOAT NOT NULL,
`timepoint` FLOAT NOT NULL, 
`cloudcover` FLOAT NOT NULL, 
`highcloud` FLOAT NOT NULL, 
`midcloud` FLOAT NOT NULL, 
`lowcloud` FLOAT NOT NULL, 
`temp2m` FLOAT NOT NULL, 
`lifted_index` FLOAT NOT NULL, 
`rh2m` FLOAT NOT NULL, 
`msl_pressure` FLOAT NOT NULL, 
`prec_amount` FLOAT NOT NULL,
`snow_depth` FLOAT NOT NULL,
`wind10m.speed` FLOAT NOT NULL,
`fecha` DATE,
PRIMARY KEY (`id_clima`, `country`),
CONSTRAINT `fk_clima_ataques`
FOREIGN KEY (`country`)
REFERENCES `ataques` (`country`) ON DELETE RESTRICT ON UPDATE CASCADE)
ENGINE = InnoDB;'''

iniciacion.crear_insertar_tabla(query_ataques)

iniciacion.crear_insertar_tabla(query_clima)


df = sp.pd.read_pickle('../files/datos_clima_attacks_clase.pkl')

print("archivo cargado")



















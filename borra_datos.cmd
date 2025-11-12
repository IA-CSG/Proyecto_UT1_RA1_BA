echo "ELIMINA LOS DATOS CREARLOS PARA VOLVER A GENERARLOS"

del project\data\drops\*.* /Q
del project\data\quarantine\*.* /Q
del project\data\storage\bronze\*.* /Q
del project\data\storage\gold\*.* /Q
del project\data\storage\silver\*.* /Q

del project\output\*.* /Q
del project\sql\*.* /Q

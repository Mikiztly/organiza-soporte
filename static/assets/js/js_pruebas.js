document.addEventListener('DOMContentLoaded', function() {
    const empresaSelect = document.getElementById('id_Empresa');
    const equipoSelect = document.getElementById('id_Equipo');
    const impresoraSelect = document.getElementById('id_Impresora');

    if (empresaSelect) {
        const ajaxUrl = empresaSelect.dataset.ajaxUrl;

        empresaSelect.addEventListener('change', function() {
            const sucursalId = this.value;
            if (!sucursalId) {
                if (equipoSelect) equipoSelect.innerHTML = '<option value="">---------</option>';
                if (impresoraSelect) impresoraSelect.innerHTML = '<option value="">---------</option>';
                return;
            }
            fetch(`${ajaxUrl}?sucursal_id=${sucursalId}`)
                .then(response => response.json())
                .then(data => {
                    console.log('Datos recibidos:', data);

                    if (data.error) {
                        console.error('Error en los datos:', data.error);
                        return;
                    }

                    // Actualizar select de equipos
                    if (equipoSelect) {
                        equipoSelect.innerHTML = '<option value="">---------</option>';
                        data.equipos.forEach(equipo => {
                            console.log('Procesando equipo:', equipo);
                            const option = document.createElement('option');
                            option.value = equipo.id;
                            option.textContent = equipo.Equipo;
                            equipoSelect.appendChild(option);
                        });
                    }

                    // Actualizar select de impresoras
                    if (impresoraSelect) {
                        impresoraSelect.innerHTML = '<option value="">---------</option>';
                        data.impresoras.forEach(impresora => {
                            console.log('Procesando impresora:', impresora);
                            const option = document.createElement('option');
                            option.value = impresora.id;
                            option.textContent = impresora.Nombre;
                            impresoraSelect.appendChild(option);
                        });
                    }
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        });
    }
});

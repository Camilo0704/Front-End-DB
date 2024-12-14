
    function limpiarFormulario() {
        document.querySelector('.Input').reset();
    }
    
    document.querySelector('.BtnLimpiar').addEventListener('click', limpiarFormulario);

    function limpiarForm() {
        document.querySelector('.Input2').reset();
    }
    
    document.querySelector('.BtnDelete').addEventListener('click', limpiarForm);

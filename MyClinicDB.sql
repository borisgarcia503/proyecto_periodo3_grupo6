USE MyClinicDB;
GO

-- Tabla Usuario (para control de acceso al sistema)
CREATE TABLE Usuario (
    IdUsuario INT IDENTITY(1,1) PRIMARY KEY,
    NombreUsuario VARCHAR(50) NOT NULL,
    Contrasena VARCHAR(255) NOT NULL,
    Rol VARCHAR(20) NOT NULL -- Ejemplo: Admin, Recepcionista, Doctor
);
GO

-- Tabla Paciente
CREATE TABLE Paciente (
    IdPaciente INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    DUI VARCHAR(15) UNIQUE,
    Telefono VARCHAR(15),
    Direccion VARCHAR(200),
    FechaNacimiento DATE
);
GO

-- Tabla Médico
CREATE TABLE Medico (
    IdMedico INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Especialidad VARCHAR(50),
    Telefono VARCHAR(15),
    Correo VARCHAR(100)
);
GO

-- Tabla Cita
CREATE TABLE Cita (
    IdCita INT IDENTITY(1,1) PRIMARY KEY,
    IdPaciente INT NOT NULL,
    IdMedico INT NOT NULL,
    FechaCita DATETIME NOT NULL,
    Motivo VARCHAR(200),
    Estado VARCHAR(20) DEFAULT 'Pendiente', -- Pendiente, Atendida, Cancelada
    FOREIGN KEY (IdPaciente) REFERENCES Paciente(IdPaciente),
    FOREIGN KEY (IdMedico) REFERENCES Medico(IdMedico)
);
GO


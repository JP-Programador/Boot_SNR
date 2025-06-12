
## 🧾 Entidades e Atributos

---

### **CLIENTES**
- Nome
- Endereço
- CPF *(PK)*
- Telefone

---

### **PLANOS**
- Nome *(PK)*

---

### **CATEGORIAS**
- Nome *(PK)*
- Nome_Amigavel

---

### **TIPO_CATEGORIA**
- Nome *(PK)*
- Descrição

---

### **RELATOS**
- Descrição
- *(Relacionamento com CLIENTES e CATEGORIAS)*

---

### **RESPOSTA_AUTOMATICA**
- Resposta
- Data_Hora

---

### **PROTOCOLO**
- Número *(PK)*
- Data_Hora
- Status

---

## 🔗 Relacionamentos

- **CLIENTES** → POSSUI → **PLANOS**
- **CLIENTES** → REGISTRA → **RELATOS**
- **PLANOS** → COBRE → **CATEGORIAS**
- **RELATOS** → CLASSIFICA → **CATEGORIAS**
- **CATEGORIAS** → PERTENCE → **TIPO_CATEGORIA**
- **RELATOS** → GERA → **RESPOSTA_AUTOMATICA**
- **RESPOSTA_AUTOMATICA** → GERA → **PROTOCOLO**

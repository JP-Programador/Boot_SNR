
### **cliente**
- `cpf` (VARCHAR(11)) **[PK]**
- `nome` (VARCHAR(100))
- `endereco` (VARCHAR(200))
- `telefone` (VARCHAR(15))
- `plano_nome` (VARCHAR(100)) **[FK → plano.nome]**

---

### **plano**
- `nome` (VARCHAR(100)) **[PK]**

---

### **planocategoria**
- `plano_nome` (VARCHAR(100)) **[PK, FK → plano.nome]**
- `categoria_nome` (VARCHAR(100)) **[PK, FK → categoria.nome]**

---

### **categoria**
- `nome` (VARCHAR(100)) **[PK]**
- `nome_amigavel` (VARCHAR(150))
- `tipo_id` (INT) **[FK → tipocategoria.id]**

---

### **tipocategoria**
- `id` (INT) **[PK]**
- `nome` (VARCHAR(100))
- `descricao` (TEXT)

---

### **relato**
- `id` (INT) **[PK]**
- `cpf_cliente` (VARCHAR(11)) **[FK → cliente.cpf]**
- `descricao` (TEXT)
- `categoria_nome` (VARCHAR(100)) **[FK → categoria.nome]**

---

### **respostaautomatica**
- `id` (INT) **[PK]**
- `relato_id` (INT) **[FK → relato.id]**
- `resposta` (TEXT)
- `data_hora` (DATETIME)

---

### **protocolo**
- `numero` (VARCHAR(20)) **[PK]**
- `data_hora` (DATETIME)
- `status` (VARCHAR(50))
- `resposta_id` (INT) **[FK → respostaautomatica.id]**

---

## 🔗 Relacionamentos

- Um **cliente** está associado a um **plano**.
- Um **relato** é feito por um **cliente** e se refere a uma **categoria**.
- Uma **resposta automática** responde a um **relato**.
- Um **protocolo** está vinculado a uma **resposta automática**.
- Uma **categoria** pertence a um **tipo de categoria**.
- Um **plano** pode cobrir múltiplas **categorias** através da tabela associativa **planocategoria**.

# Simulación del registro de la empresa en New Jersey: dos opciones

> Versión 1.0 · 8 de octubre de 2026 · Equipo Asesor (ver [prompt maestro](PROMPT-MAESTRO-EQUIPO-ASESOR.md))
> Empresa ficticia usada en la simulación: **"Andes Digital Studio LLC"**. Los nombres, direcciones y números son ejemplos, no datos reales.
> **ESTIMACIÓN** = rango de mercado, no tarifa oficial. **VERIFICAR** = dato que puede cambiar o que depende del caso; confirmar con un CPA en EE. UU. y un contador en Colombia.

| | **Opción 1** | **Opción 2** |
|---|---|---|
| Socios | Emiro (Colombia), 100% | Socio US (ciudadano estadounidense, residente en NJ) + Emiro (Colombia) |
| Tipo de entidad | LLC de un miembro (disregarded entity, dueño extranjero) | LLC de dos miembros (partnership por defecto) |
| Quién firma y tramita | Emiro, a distancia | El socio US (tiene SSN y está en NJ) |
| Tiempo hasta facturar | 3 a 6 semanas (ESTIMACIÓN) | 1 a 3 semanas (ESTIMACIÓN) |
| Costo de arranque | USD 700 – 2.000 (ESTIMACIÓN) | USD 1.200 – 3.500 (ESTIMACIÓN) |
| Costo anual de cumplimiento | USD 500 – 1.500 (ESTIMACIÓN) | USD 1.500 – 4.000 (ESTIMACIÓN) + impuestos |

Se supone que el socio US vive en New Jersey. Si vive en otro estado y trabaja desde allí, la LLC probablemente también tendría que registrarse como "foreign LLC" en ese estado (VERIFICAR).

---

## Opción 1: Emiro como único socio, desde Colombia

### Documentos que Emiro debe tener listos
- Pasaporte vigente (escaneado a color).
- Correo y teléfono de contacto; dirección de residencia en Colombia.
- RUT colombiano (para el contador en Colombia).
- Tarjeta de crédito internacional para pagar tarifas del estado.

### Simulación paso a paso

**Día 1. Nombre y agente registrado**
1. Buscar el nombre "Andes Digital Studio LLC" en el Business Name Search del portal de NJ (njportal.com/DOR/BusinessFormation). Debe terminar en "LLC", "L.L.C." o "Limited Liability Company".
2. Contratar un **agente registrado** con dirección física en NJ (no se acepta apartado postal). Costo: USD 50 – 300 al año (ESTIMACIÓN).
3. Contratar una **dirección comercial virtual** en NJ para correspondencia y para los registros de Meta, Google y bancos. Costo: USD 10 – 50 al mes (ESTIMACIÓN).

**Día 1 o 2. Certificate of Formation (en línea)**
Campos que se llenan en el portal de NJ (ejemplo):

| Campo | Valor de ejemplo |
|---|---|
| Business type | Domestic Limited Liability Company |
| Business name | Andes Digital Studio LLC |
| Registered agent | [Nombre del proveedor], [dirección física en NJ] |
| Main business address | Dirección comercial virtual en NJ |
| Business purpose | Digital marketing, web design and development, graphic design, consulting, e-commerce and any lawful purpose |
| Members / managers | Emiro [apellido], Member, dirección en Colombia |
| Signature | Emiro, Authorized Representative |
| Fee | **USD 100** (oficial, nj.gov/treasury/revenue/fees.shtml) |

Resultado: Certificate of Formation aprobado y número de entidad de NJ. En línea suele aprobarse de inmediato o en pocos días (ESTIMACIÓN).

**Día 2. Operating Agreement de un miembro**
Documento privado, no se presenta al estado. Cláusulas mínimas: propiedad 100% de Emiro, gestión por el miembro (member-managed), responsabilidad limitada, cuentas bancarias separadas, cesión de propiedad intelectual a la LLC, admisión futura de socios (para poder pasar a la Opción 2 sin rehacer todo), disolución. Costo: USD 0 (plantilla) a USD 800 (abogado) (ESTIMACIÓN).

**Días 3 a 10. EIN del IRS (Form SS-4)**
Emiro no tiene SSN ni ITIN, así que no puede usar el formulario en línea. Opciones: llamar a la línea internacional del IRS (+1 267-941-1099, horario de oficina del este de EE. UU.) y obtener el EIN en la misma llamada, o enviar el SS-4 por fax (respuesta en días o semanas) (ESTIMACIÓN).

| Línea del SS-4 | Valor de ejemplo |
|---|---|
| 1. Legal name | Andes Digital Studio LLC |
| 4a–4b. Mailing address | Dirección comercial virtual en NJ |
| 7a. Responsible party | Emiro [apellido] |
| 7b. SSN/ITIN/EIN | "Foreign" (no tiene) |
| 8a–8c. Is this an LLC? / Number of members | Yes / 1 |
| 9a. Type of entity | Other: "Foreign-owned U.S. disregarded entity", y se marca Form 1120 |
| 10. Reason | Started new business: digital marketing services |
| 16. Principal activity | Other: digital marketing and web design services |

Resultado: carta CP 575 con el EIN. Costo: USD 0.

**Días 5 a 15. NJ-REG y Business Registration Certificate**
Con el EIN se presenta el Form NJ-REG en el portal de DORES. Registra la empresa ante la División de Impuestos (sales tax si va a vender productos o servicios gravables) y como empleador si algún día contrata en NJ. Resultado: Business Registration Certificate (BRC). Sin costo publicado.

**Días 10 a 30. Banco y pagos**
1. Solicitar cuenta empresarial en una fintech que acepte dueños no residentes (por ejemplo Mercury, Relay o Wise Business; la aceptación cambia, VERIFICAR). Se suben: Certificate of Formation, EIN (CP 575), Operating Agreement, pasaporte, prueba de dirección y descripción del negocio y de los clientes.
2. Abrir Stripe y PayPal Business con la cuenta bancaria de la LLC.
3. Verificar la empresa en Meta Business Manager y como anunciante en Google Ads con el nombre exacto de la LLC, el dominio y la misma dirección.

**Días 20 a 45. Listo para facturar**
Contrato marco (MSA) y orden de trabajo (SOW), facturación en QuickBooks, Xero, Wave o Invoice Ninja, y a los clientes de EE. UU. se les entrega un W-8BEN del propietario con el EIN de la LLC (no un W-9) (VERIFICAR con CPA).

### Obligaciones anuales de la Opción 1

| Obligación | Ante quién | Plazo | Costo |
|---|---|---|---|
| Annual Report | NJ DORES | Último día del mes de aniversario de la formación | **USD 75** (oficial) |
| Form 5472 + Form 1120 pro forma | IRS | 15 de abril (prórroga con Form 7004) | Preparador: USD 300 – 1.000 (ESTIMACIÓN). **Multa por no presentarlo: USD 25.000** |
| Declaraciones de NJ | NJ Division of Taxation | Según el caso | VERIFICAR con CPA |
| Sales tax (solo si vende productos o servicios gravables en NJ, 6.625%) | NJ Division of Taxation | Según la frecuencia asignada | Lo pagan los clientes |
| Renta, activos en el exterior y régimen cambiario | DIAN y Banco de la República | Calendario de Colombia | Contador colombiano (ESTIMACIÓN) |
| Renovar agente registrado y dirección virtual | Proveedores | Anual | USD 170 – 900 (ESTIMACIÓN) |

**Impuesto federal:** si todo el trabajo se hace desde Colombia y la LLC no tiene empleados, oficina ni representante en EE. UU., normalmente no hay impuesto federal sobre la renta y toda la utilidad tributa en Colombia (VERIFICAR con CPA).

---

## Opción 2: dos socios, el socio US (ciudadano americano, en NJ) y Emiro (Colombia)

### Decisión previa: porcentajes y roles
- Ejemplo: 50% / 50%, o 51% / 49% para evitar empates. Con 50/50 el Operating Agreement **debe** incluir un mecanismo de desempate (mediador, voto de calidad por área, o compra-venta forzada tipo "shotgun").
- Gestión recomendada: **manager-managed**, con el socio US como manager para trámites locales y banca, y Emiro como manager con autoridad sobre operación digital y finanzas. Firmas conjuntas para gastos mayores de un monto acordado.

### Documentos que cada socio debe tener listos
- **Socio US:** licencia de conducir o pasaporte de EE. UU., **SSN**, dirección de residencia en NJ.
- **Emiro:** pasaporte, dirección en Colombia, RUT. Más adelante, ITIN (Form W-7, normalmente junto con su primera declaración 1040-NR).

### Simulación paso a paso

**Día 1. Nombre, agente y dirección**
1. Business Name Search, igual que en la Opción 1.
2. Agente registrado: puede ser el propio socio US con su dirección en NJ (USD 0), aunque su dirección quedará pública. Alternativa: proveedor, USD 50 – 300 al año (ESTIMACIÓN).
3. Dirección comercial: la del socio US o una oficina virtual.

**Día 1. Certificate of Formation (en línea)**

| Campo | Valor de ejemplo |
|---|---|
| Business type | Domestic Limited Liability Company |
| Business name | Andes Digital Studio LLC |
| Registered agent | Socio US o proveedor, dirección física en NJ |
| Main business address | Dirección en NJ |
| Members / managers | Socio US (Manager, NJ) y Emiro (Manager, Colombia) |
| Signature | Socio US, Authorized Representative |
| Fee | **USD 100** (oficial) |

**Día 1. EIN en línea (inmediato)**
El socio US actúa como "responsible party" con su SSN y obtiene el EIN en línea en la misma sesión. En el SS-4 en línea: LLC con 2 miembros, se trata como partnership. Costo: USD 0.

**Días 1 a 7. Operating Agreement de dos miembros**
Recomendable con abogado de NJ. Cláusulas esenciales:
- Aportes de cada socio (dinero, equipos, cartera de clientes, trabajo) y porcentajes.
- Reparto de utilidades y de pérdidas, y **distribuciones para impuestos** (tax distributions), porque cada socio paga impuestos sobre su parte aunque no reciba dinero.
- Retenciones al socio extranjero: autorización para que la LLC retenga y pague por cuenta de Emiro el impuesto federal (sección 1446) y el de NJ.
- Roles, firmas y límites de gasto. Mecanismo de desempate.
- Propiedad intelectual de la LLC; no competencia y no captación de clientes.
- Salida de un socio, muerte o incapacidad, valoración y derecho de compra preferente.
- Elección del "Partnership Representative" ante el IRS (normalmente el socio US).
Costo: USD 500 – 1.500 (ESTIMACIÓN).

**Días 2 a 10. NJ-REG y Business Registration Certificate**
Igual que en la Opción 1, presentado por el socio US.

**Días 3 a 15. Banco y pagos**
El socio US abre la cuenta empresarial en un banco tradicional o fintech (en persona si es banco). Emiro se agrega como firmante con su pasaporte (algunos bancos exigen que todos los firmantes con más del 25% se identifiquen; VERIFICAR con el banco). Luego Stripe, PayPal, Meta y Google, igual que en la Opción 1. A los clientes de EE. UU. se les entrega un **W-9** de la LLC.

**Días 7 a 20. Listo para facturar**

### Obligaciones anuales de la Opción 2

| Obligación | Ante quién | Plazo | Costo o tasa |
|---|---|---|---|
| Annual Report | NJ DORES | Mes de aniversario | **USD 75** (oficial) |
| Form 1065 + K-1 a cada socio | IRS | 15 de marzo | Preparador: USD 1.000 – 2.500 (ESTIMACIÓN) |
| Retención sección 1446 sobre la parte de Emiro (Forms 8804, 8805 y pagos trimestrales 8813) | IRS | Trimestral y anual | Tasa máxima de individuos (actualmente 37%) sobre la utilidad asignada a Emiro, acreditable en su 1040-NR (VERIFICAR) |
| Form NJ-1065 | NJ Division of Taxation | 15 de abril (día 15 del cuarto mes) | Tarifa de USD 150 por socio **solo si hay más de dos socios**: con dos socios no aplica (fuente: NJ TB-55) |
| Form NJ-CBT-1065 (impuesto por el socio no residente) | NJ Division of Taxation | 15 de abril, con pagos trimestrales del 25% | **6.37%** de la parte de Emiro de la renta de NJ (fuente: NJ TB-55), acreditable en su declaración de NJ |
| Form 1040-NR de Emiro (con ITIN) y declaración no residente de NJ | IRS y NJ | 15 de junio si no tiene salario en EE. UU. (VERIFICAR) | Preparador: USD 300 – 800 (ESTIMACIÓN) |
| Declaración personal del socio US (Schedule K-1, impuesto de autoempleo 15.3% sobre su parte si trabaja activamente) | IRS y NJ | 15 de abril | Según su caso |
| Renta en Colombia de Emiro, con descuento por impuestos pagados en EE. UU. | DIAN | Calendario de Colombia | Contador colombiano (ESTIMACIÓN) |
| Sales tax si aplica (6.625%) | NJ Division of Taxation | Según frecuencia | Lo pagan los clientes |

**Por qué hay impuestos en EE. UU. en esta opción:** el socio US trabaja para la LLC desde NJ, así que la LLC tiene un negocio en EE. UU. y toda su utilidad, incluida la parte de Emiro, queda sujeta al impuesto federal y al de NJ. Emiro luego descuenta en Colombia lo que pagó en EE. UU. (VERIFICAR límites con contador colombiano, porque no hay tratado de doble imposición).

### Alternativas de estructura para la Opción 2
- **S-corp: no es posible** mientras Emiro, no residente, sea socio.
- **Elegir tributar como C-corp** (Form 8832): la empresa paga 21% federal más el impuesto corporativo de NJ (CBT) y elimina las retenciones de socio extranjero. Pero los dividendos a Emiro tendrían retención del 30% (sin tratado). Conviene evaluarlo solo si se van a reinvertir casi todas las utilidades (VERIFICAR con CPA).
- **Emiro como contratista en lugar de socio:** la LLC es solo del socio US y paga a Emiro por servicios prestados desde Colombia. Más simple en impuestos, pero Emiro pierde la propiedad y el control.

---

## Comparación final

| Criterio | Opción 1: socio único en Colombia | Opción 2: socio US + socio en Colombia |
|---|---|---|
| Velocidad de arranque | Más lenta (EIN y banco a distancia) | Más rápida (EIN en línea y banco presencial) |
| Costo de arranque | Más bajo | Medio |
| Costo anual | Bajo | Medio-alto (1065, 1446, NJ-CBT-1065, 1040-NR) |
| Impuestos en EE. UU. | Normalmente cero si todo se hace desde Colombia (VERIFICAR) | Sí, sobre toda la utilidad |
| Control | Total de Emiro | Compartido; depende del Operating Agreement |
| Banca, crédito y credibilidad local | Media | Alta |
| Ventas presenciales en NJ/NY | Limitadas | Plenas |
| Riesgo principal | Olvidar el Form 5472 (multa de USD 25.000) | Conflicto entre socios y errores de retención |

**Recomendación del equipo:** si el socio US va a vender y atender clientes en persona, la Opción 2 genera más negocio y justifica su mayor costo. En ese caso se debe invertir en un buen Operating Agreement y en un CPA desde el primer mes. Si el socio US todavía no está confirmado o solo aportaría su dirección, conviene empezar con la Opción 1 y dejar en el Operating Agreement la puerta abierta para admitirlo después.

---

## Fuentes oficiales
- Tarifas de NJ DORES (formación USD 100, annual report USD 75, actualizado 07/01/26): https://www.nj.gov/treasury/revenue/fees.shtml
- Registro en NJ (formación, NJ-REG, BRC): https://www.nj.gov/treasury/revenue/gettingregistered.shtml
- Portal de formación: https://www.njportal.com/DOR/BusinessFormation/
- NJ TB-55, Partnership Filing Fee and Nonresident Partner Tax (USD 150 por socio si hay más de dos; 6.37% socios no residentes individuales, 9% corporativos): https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb55.pdf
- IRS, Form SS-4 y EIN: https://www.irs.gov/forms-pubs/about-form-ss-4
- IRS, Form 5472: https://www.irs.gov/forms-pubs/about-form-5472
- IRS, retención a socios extranjeros (sección 1446): https://www.irs.gov/individuals/international-taxpayers/partnership-withholding
- IRS, ITIN (Form W-7): https://www.irs.gov/forms-pubs/about-form-w-7
- FinCEN, BOI (empresas creadas en EE. UU. exentas desde marzo de 2025): https://www.fincen.gov/boi

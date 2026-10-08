# Guía operativa: cliente de limpieza en Washington

> Versión 1.0 · 8 de octubre de 2026 · Equipo Asesor (@Juridico, @Contador, @Admin; ver [prompt maestro](PROMPT-MAESTRO-EQUIPO-ASESOR.md))
> Ejercicio: una empresa de limpieza en el estado de Washington contrata a Emiro para publicidad, página web, diseño gráfico, estrategia de marketing digital y manejo de redes sociales.
> **VERIFICAR** = depende del caso o puede haber cambiado; confirma con un CPA de EE. UU. y un contador público en Colombia. **ESTIMACIÓN** = no es un dato oficial. Las normas colombianas y las de Washington aquí citadas vienen de resultados de búsqueda de fuentes secundarias y de la DIAN, no del texto oficial completo.
> Contrato listo para adaptar: [CONTRATO-SERVICIOS-CLIENTE-WASHINGTON.md](CONTRATO-SERVICIOS-CLIENTE-WASHINGTON.md)

---

## 1. Primero: ¿quién firma el contrato y quién factura?

Todo lo demás depende de esta decisión. Hay dos rutas para este cliente:

| | **Ruta A: factura una empresa o persona en Colombia** | **Ruta B: factura la LLC de New Jersey** |
|---|---|---|
| Proveedor | Persona natural o SAS colombiana | LLC de un solo miembro (dueño en Colombia) |
| Factura | Factura electrónica DIAN de exportación de servicios | Factura comercial en USD (PDF, QuickBooks, etc.) |
| Formulario para el cliente | W-8BEN (persona) o W-8BEN-E (empresa) | W-9 de la LLC (o W-8BEN del dueño si es disregarded; VERIFICAR con CPA) |
| IVA / sales tax | Exportación de servicios: exenta de IVA colombiano (con requisitos) | Sin IVA en EE. UU.; revisar sales tax de Washington (sección 4) |
| Declaración en EE. UU. | Ninguna normalmente | Form 5472 + 1120 pro forma cada año; multa USD 25.000 si se omite |
| Declaración en Colombia | Renta (y IVA si eres responsable) | Renta del dueño (la LLC es transparente) y reportes cambiarios |
| Costo de mantenimiento | Contador colombiano | Contador colombiano + CPA en EE. UU. + agente registrado |
| Mejor cuando | Pocos clientes de EE. UU., contratos pequeños | Cliente exige proveedor con entidad en EE. UU., W-9, pagos ACH y seguro |

**Recomendación del equipo para este ejercicio:** un cliente local de limpieza (pyme) normalmente acepta a un proveedor extranjero con W-8BEN, así que **Ruta A** es la más barata para empezar. Si el cliente pide un W-9, pagos ACH o certificado de seguro, o si vas a tener varios clientes en EE. UU., pasa a la **Ruta B**. Las secciones 2 a 7 explican cada ruta.

---

## 2. Facturación electrónica

### Ruta A: desde Colombia (DIAN)
1. **Inscribirte en el RUT** con la responsabilidad de **exportador de servicios** (persona natural o jurídica). Sin esa inscripción no puedes acreditar la exención.
2. **Habilitarte como facturador electrónico** ante la DIAN (en el servicio "Factura electrónica": habilitación, set de pruebas y numeración). Puedes usar el facturador gratuito de la DIAN o un proveedor tecnológico (Siigo, Alegra, World Office y otros; ESTIMACIÓN: USD 10 a 40 al mes).
3. **Emitir la factura electrónica de venta de exportación de servicios** a nombre del cliente de Washington. Debe indicar: el valor del servicio, el país de destino (Estados Unidos), la descripción del servicio, y el nombre o razón social del adquirente en el exterior con su domicilio. Envía el PDF y el XML al cliente.
4. **Moneda:** puedes facturar en USD con la tasa representativa del mercado (TRM) del día de la factura.
5. **Conservar los soportes:** contrato, factura, correos, reportes y comprobante de pago. Si no puedes acreditar los requisitos, respondes por el IVA no facturado.

Fuente: art. 481 literal c) del Estatuto Tributario y conceptos de la DIAN (normograma.dian.gov.co). Los servicios deben prestarse desde Colombia y usarse exclusivamente en el exterior, por una empresa sin negocios en Colombia. Marketing para una empresa de Washington dirigido a clientes de Washington cumple ese perfil (VERIFICAR con tu contador).

### Ruta B: desde la LLC de New Jersey (EE. UU.)
- **EE. UU. no tiene factura electrónica obligatoria** ni ente regulador de facturas. Basta una factura comercial clara: nombre y dirección de ambas partes, número de factura, fecha, descripción del servicio, monto, impuestos si aplican, términos y datos de pago.
- Usa QuickBooks, Wave, Invoice Ninja (de código abierto) o Xero para generarla y llevar la cartera.
- Pide el pago por **ACH** o Stripe/tarjeta a la cuenta bancaria empresarial de la LLC.

---

## 3. Impuestos anuales: renta e IVA

### Colombia (aplica a las dos rutas)
| Tema | Qué hacer | Plazo aproximado | Notas |
|---|---|---|---|
| **Declaración de renta anual** | Declarar todos los ingresos del año, incluidos los del exterior. Persona natural: según los últimos dígitos del NIT. SAS: en abril o mayo | Persona natural: agosto a octubre. Persona jurídica: abril a mayo (VERIFICAR el calendario del año) | Régimen ordinario o **Régimen Simple de Tributación** (RST), que puede servir si facturas poco; VERIFICAR |
| **IVA** | Las exportaciones de servicios están **exentas con derecho a devolución**, pero si eres responsable de IVA presentas la declaración periódica (bimestral o cuatrimestral según tus ingresos) | VERIFICAR | Si solo exportas, el IVA en tus compras puede devolverse |
| **Retención en la fuente / ICA** | No aplica retención por un cliente extranjero. Revisa el impuesto de industria y comercio (ICA) de tu municipio | Según el municipio | Las exportaciones de servicios pueden tener tratamiento especial en ICA; VERIFICAR |
| **Reporte cambiario** | Los servicios no obligan a canalizar por el mercado cambiario, pero si el dinero entra por un banco o plataforma que pide declaración de cambio, conserva el soporte | Al recibir el pago | VERIFICAR con tu banco |
| **Activos en el exterior (Ruta B)** | Declarar la LLC y su cuenta bancaria como activos en el exterior si superan el umbral | Con la renta | VERIFICAR con contador colombiano |

### Estados Unidos
| Ruta | Obligación | Detalle |
|---|---|---|
| **A** | Normalmente ninguna | El cliente de Washington no te retiene si le das el **W-8BEN** y el servicio se presta fuera de EE. UU. Si trabajas físicamente en EE. UU., cambia (retención del 30% sin tratado) |
| **B** | **Form 5472 + 1120 pro forma** cada año | Aunque no tengas ingresos. Plazo habitual: 15 de abril (prórroga con Form 7004). Multa de USD 25.000 si no se presenta |
| **B** | **Impuesto federal** | Normalmente cero si todo se hace desde Colombia y la LLC no tiene presencia en EE. UU. (VERIFICAR con CPA) |
| **B** | **New Jersey** | Annual Report de USD 75 cada año en DORES (fuente: nj.gov) |

### Impuestos del cliente
- El cliente puede deducir lo que te paga como gasto de negocio con tu factura y el comprobante de pago.
- Si le facturas desde la LLC y supera el límite, el cliente te reporta en un **1099-NEC** (el límite anual subió a USD 2.000 desde 2026; VERIFICAR). Con W-8BEN no lo hace.

---

## 4. Washington: impuestos al servicio (punto crítico)

Washington **no tiene impuesto estatal sobre la renta de personas**, pero sí tiene **retail sales tax** (impuesto a las ventas, base estatal del 6,5% más tasas locales) y el impuesto **B&O** (sobre ingresos brutos).

**Cambio reciente:**
- Desde el **1 de octubre de 2025**, la ley ESSB 5814 incluyó en el retail sales tax los **servicios de publicidad**, los **servicios de tecnología (TI)** y el **desarrollo de sitios web a medida** (el diseño, desarrollo y soporte de un sitio web, y también la consultoría y capacitación web). El hosting y el registro de dominios están excluidos de "publicidad".
- En 2026 la ley SB 6346 prevé **derogar** el impuesto a TI y desarrollo web a medida a partir del **1 de enero de 2029**, pero esa derogación depende de otras condiciones legales. **La publicidad sigue gravada.** Hay demandas pendientes contra parte de la expansión.

**Qué significa para este contrato:**
- Tus servicios de **publicidad** (campañas, gestión de anuncios, redes) y de **página web a medida** pueden estar gravados cuando el cliente está en Washington.
- Como proveedor fuera del estado, la obligación de cobrar el impuesto depende de tu **nexo económico**: registrarte en Washington (licencia de negocio, UBI) y reportar B&O si tus ingresos de Washington superan **USD 100.000** en el año actual o el anterior. Por debajo de ese monto y sin presencia física, normalmente no tienes que cobrarlo.
- Si no cobras el impuesto, el **cliente** puede deber el **use tax** por su cuenta. Es la razón por la que la cláusula 3.6 del contrato reparte esta responsabilidad.
- Algunos servicios (diseño gráfico puro, estrategia y consultoría) pueden quedar fuera. Clasificar cada servicio es trabajo para un CPA con experiencia en impuestos de Washington.

**Acción:** para un primer cliente pequeño, deja el impuesto fuera de tus precios, déjalo claro en el contrato y consulta a un CPA una vez antes de firmar. Vuelve a revisar el tema con tu CPA cuando los ingresos de clientes de Washington se acerquen a USD 100.000 al año. (Fuentes: Washington Department of Revenue, dor.wa.gov, y resúmenes de Morgan Lewis, PwC y Ballard Spahr; VERIFICAR el texto vigente.)

---

## 5. Representante legal, socios y registro

### Ruta A (Colombia)
| Figura | Qué es | Trámite |
|---|---|---|
| **Persona natural comerciante** | Tú solo, sin sociedad | Matrícula mercantil en la **Cámara de Comercio** + RUT. Costo de matrícula según tus activos (ESTIMACIÓN: desde unos COP 300.000 a 700.000) |
| **SAS** (Sociedad por Acciones Simplificada) | Sociedad con uno o más socios (accionistas); responsabilidad limitada | Documento privado de constitución (no exige escritura pública, salvo aportes de inmuebles), registro en Cámara de Comercio y RUT. Nombra un **representante legal** (puede ser el único accionista) |

- **Renovación de la matrícula mercantil:** cada año, a más tardar el **31 de marzo** (VERIFICAR).
- **Representante legal:** firma contratos y facturas a nombre de la SAS. Lo acredita el certificado de existencia y representación legal de la Cámara de Comercio.
- **Socios:** para este ejercicio, Emiro es único accionista. Un socio adicional se incorpora cambiando el libro de accionistas y registrándolo en la Cámara.

### Ruta B (New Jersey)
| Figura | Qué es | Trámite |
|---|---|---|
| **LLC** | Sociedad de responsabilidad limitada | Certificate of Formation en NJ DORES (USD 100), agente registrado, EIN del IRS, NJ-REG, Operating Agreement. Ver [simulación de registro](SIMULACION-REGISTRO-DOS-OPCIONES.md) |
| **Representante legal** | En una LLC el "member" o "manager" tiene autoridad para firmar. El Operating Agreement la define | Firma contratos como "Member" o "Manager" |
| **Socios** | "Members" de la LLC; entran o salen mediante el Operating Agreement | Si entra un socio, la LLC pasa a ser partnership para efectos fiscales (1065); ver la simulación |

### Washington (el cliente)
- Es un negocio con su propia licencia en Washington (UBI, Business Licensing Service). Pídele su nombre legal exacto y UBI para el contrato.
- **Tú no necesitas registrar nada en Washington** mientras no superes los umbrales de la sección 4.

---

## 6. Notarización y documentos

| Documento | ¿Notario? | Qué hacer |
|---|---|---|
| Contrato de servicios con el cliente (EE. UU.) | **No**. Basta firma electrónica (DocuSign, Dropbox Sign) | Firma el representante de cada parte; guarda el PDF firmado |
| Operating Agreement de la LLC | No es obligatorio | Firma de los miembros; el banco puede pedirla |
| Constitución de la SAS (Colombia) | No exige notario (documento privado) | Reconocimiento de firmas ante notario solo si un tercero lo pide |
| Documentos colombianos que deban usarse en EE. UU. (por ejemplo, certificado de la Cámara de Comercio para el banco o para el cliente) | Sí: **apostilla** (en la Cancillería de Colombia) y, si hay que traducirlos, **traducción oficial** | Apostilla en línea; traducción por traductor oficial (ESTIMACIÓN: USD 30 a 80 por página) |
| Documentos de EE. UU. que deban usarse en Colombia (por ejemplo, certificado de la LLC) | Apostilla del estado emisor (Secretary of State o, en NJ, el servicio de apostilla de DORES) y traducción oficial | VERIFICAR el trámite de apostilla de NJ |
| Poder para que otra persona actúe por ti | Sí: poder notariado y apostillado | Define alcance y vigencia |

---

## 7. Pólizas de seguro y contadores

### Pólizas
| Póliza | Para qué | Cuándo | Costo (ESTIMACIÓN) |
|---|---|---|---|
| **Errores y omisiones / responsabilidad profesional** | Cubre reclamos si un error tuyo daña al cliente (campaña, web, datos) | Cliente grande o contrato que lo exija | USD 400 a 1.500 al año |
| **Responsabilidad civil general (CGL)** | Daños a terceros | Útil con oficina o clientes presenciales | USD 300 a 1.000 al año |
| **Ciber (cyber liability)** | Brechas de datos, hackeo de sitios y cuentas | Si manejas datos de clientes de tu cliente | USD 500 a 2.000 al año |
| **Cliente de limpieza** | El cliente debe tener su propio seguro, bonding y licencias; tú no los cubres | Pídele el certificado si lo vas a anunciar como "asegurado y garantizado" | A cargo del cliente |

- En Colombia, para un servicio digital no se exige póliza; una póliza de cumplimiento solo se pide en contratos con entidades públicas.
- Si el contrato dice que mantendrás seguro, tenlo antes de firmar.

### Contadores
| Quién | Para qué | Costo (ESTIMACIÓN) |
|---|---|---|
| **Contador público en Colombia** | Renta, IVA, RUT, factura electrónica, régimen cambiario, activos en el exterior | COP 200.000 a 600.000 al mes, según el volumen |
| **CPA en EE. UU.** (Ruta B) | Form 5472 + 1120, EIN, NJ, impuestos de Washington, 1099/W-8/W-9 | USD 300 a 1.500 al año |
| **Teneduría mensual** | Registrar ingresos y gastos, conciliar el banco | Software USD 15 a 50 al mes, o contador |

---

## 8. Lista de pasos para este ejercicio (orden recomendado)

1. Decidir la ruta (A o B) con tu contador colombiano y, si es B, con el CPA de EE. UU.
2. Pedir al cliente: nombre legal, UBI, dirección, correo de facturación y quién aprueba.
3. Adaptar el [contrato](CONTRATO-SERVICIOS-CLIENTE-WASHINGTON.md) y el SOW; que lo revise un abogado.
4. Preparar el formulario fiscal: W-8BEN/W-8BEN-E (Ruta A) o W-9 (Ruta B).
5. Dejar listos los soportes: RUT con exportador de servicios y facturador electrónico (A), o LLC, EIN, banco y Stripe (B).
6. Firmar con firma electrónica y recibir el anticipo.
7. Crear las cuentas de anuncios a nombre del cliente y pedir acceso como administrador.
8. Entregar mensualmente: factura, reporte y llamada.
9. Cada año: renta (Colombia), renovación de matrícula (31 de marzo) o Annual Report de NJ (USD 75) y Form 5472 (Ruta B), y revisar los umbrales de Washington.

## 9. Fuentes
- DIAN, normograma y conceptos sobre exportación de servicios (art. 481 literal c del Estatuto Tributario): https://normograma.dian.gov.co
- Washington Department of Revenue, umbrales de nexo: https://dor.wa.gov/nexus
- Resumen de la expansión del sales tax de Washington (ESSB 5814): https://www.morganlewis.com/pubs/2025/05/washington-state-expands-sales-and-use-tax-to-digital-ads-and-high-tech-and-it-services
- Cambios de 2026 (SB 6346): https://www.ballardspahr.com/insights/alerts-and-articles/2026/04/washington-state-2026-session-legislature-repeals-and-rolls-back-certain-recently-enacted-taxes
- NJ DORES, tarifas: https://www.nj.gov/treasury/revenue/fees.shtml
- IRS, Form 5472: https://www.irs.gov/forms-pubs/about-form-5472

Задание: https://github.com/Santa42/HSE/tree/master/lab3

### Топология

Я добавила 2 машины с Ubuntu 21.04 для тестирования системы, поэтому фактически заявленной схеме не соответствую. Но эти машины можно просто удалить или можно удалить PC.

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/схема.jpg" width="500" height="500">

Конфигурации с сетевых устройств лежат в директории configs (r2_config.txt, r3_config.txt, r4_config.txt, vyos_config.txt, vyos2_config.txt).

Экспорт лабы лежит в этой директории (_Exports_unetlab_export-20221209-183433.zip).

____

### DHCP-сервер, выводы с устройств, подтверждающие работоспособность конфигурации:

Все клиенты получают сетевые настройки по DHCP: IP-адресс, маску сети, DNS-сервер, Default Gateway. В настройках DHCP-сервера исключены первые 10 IP-адресов из выдачи клиентам.

#### Vyos2
```
show interfaces
```
<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/vyos2_interfaces.jpg" width="600" height="300">

#### Vyos
```
show interfaces
```
<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/vyos_interfaces.jpg" width="600" height="300">

```
show service dhcp-server
```
<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/vyos_dhcp_first.jpg" width="400" height="500">
<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/vyos_dhcp_second.jpg" width="400" height="500">

#### PC получили верные настройки:

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/dhcp_work.jpg" width="600" height="600">

____

### NAT, выводы с устройств, подтверждающие работоспособность конфигурации:

На маршрутизаторе с сетями клиентов настроена технология NAT, таким образом, чтобы клиенты могли обратиться к верхнему маршрутизатору и получить ответ. На верхнем маршрутизаторе нет дополнительных маршрутов в сети клиентов.

#### Vyos
```
show nat source
```
<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/vyos_nat_source.jpg" width="400" height="500">

Пример:

- с помощью утилиты Netcat успешно подключились с ubuntu8 к vyos2, успешно подключились с ubuntu9 к vyos2, не получилось подключиться с vyos2 к ubuntu8, успешно подключились с ubuntu9 к ubuntu8 (показали, что конфигурации из дз1 все еще работают),

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/exp1.jpg" width="1000" height="500">

- с помощью wireshark убедились, что NAT работает, IP-адреса внутренних сетей заменяются на внешний IP-адрес с разными портами.

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/exp2.jpg" width="1000" height="500">

#### Vyos
```
show nat source translations detail
```
<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/vyos_nat_translations.jpg" width="600" height="150">

Пинги с vyos2 не доходят до внутренних IP-адресов:

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/vyos2_unreachable.jpg" width="600" height="150">

На верхнем маршрутизаторе нет дополнительных маршрутов в сети клиентов:

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw3/images/vyos2_ip_route.jpg" width="500" height="300">


P.S. Почему-то vyos после запуска остается со значком прогрузки, я не дожидалась, когда значок исчезнет, и все проделанные действия, все равно, давали такие же результаты, все работало. Если потом его выключить, он почему-то не включается. Чтобы включить, надо сначала сделать wipe роутеров, потом уже сделать start. 







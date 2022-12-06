Задание: https://github.com/Santa42/HSE/tree/master/lab1

### Топология

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/схема.jpg" width="400" height="500">

Конфигурации с сетевых устройств лежат в директории configs (r2_config.txt, r3_config.txt, r4_config.txt, vyos_config.txt).

Экспорт лабы лежит в этой директории (_Exports_unetlab_export-20221206-233810.zip).

____

## Выводы с устройств, подтверждающие работоспособность конфигурации:

### R2

```
show vlan
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r2vlan.jpg" width="600" height="400">

```
show interfaces trunk
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r2trunk.jpg" width="600" height="300">

```
show spanning-tree
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r2spanning-tree.jpg" width="600" height="600">

____

### R3

```
show vlan
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r3vlan.jpg" width="600" height="400">

```
show interfaces trunk
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r3trunk.jpg" width="600" height="300">

```
show spanning-tree
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r3spanning-tree.jpg" width="600" height="600">

____

### R4

```
show vlan
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r4vlan.jpg" width="600" height="400">

```
show interfaces trunk
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r4trunk.jpg" width="600" height="300">

```
show spanning-tree
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/r4spanning-tree.jpg" width="600" height="600">

____

### Vyos

```
show interfaces
```

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/vyos.jpg" width="600" height="300">

____

### Клиенты могут отправить друг другу PING

<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/pingpc5.jpg" width="800" height="300">
<img src="https://github.com/AnyaAkhmatova/nets/blob/main/hw1/images/pingpc6.jpg" width="800" height="300">






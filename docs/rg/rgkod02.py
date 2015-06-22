# jeżeli jesteś w środku, broń się
if self.location == rg.CENTER_POINT:
    return ['guard']

# LUB

# jeżeli jesteś w środku, popełnij samobójstwo
if self.location == rg.CENTER_POINT:
    return ['suicide']

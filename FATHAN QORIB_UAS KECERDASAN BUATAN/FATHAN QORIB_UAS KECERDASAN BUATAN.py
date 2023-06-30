from matplotlib import pyplot as plt
import os

class BaseFuzzy():

    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)
    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)

class Speed(BaseFuzzy):

    def __init__(self):
        self.s1 = 20
        self.s2 = 40
        self.s3 = 60
        self.s4 = 80
        self.sn = 100

    def slow(self, x):
        # 0 - s1 = 1
        # s1 - s2 = down
        if x < self.s1:
            return 1
        elif self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.down(x)
        else:
            return 0
        
    def steady(self, x):
        # s1 - s2 = up
        # s2 - s3 = 1
        # s3 - s4 = down
        if self.s1 <= x <= self.s2:
            self.minimum = self.s1
            self.maximum = self.s2
            return self.up(x)
        if self.s2 <= x <= self.s3:
            return 1
        if self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.down(x)
        else:
            return 0
        
    def fast(self, x):
        # s3 - s4 =up
        # s4 - ... = 1
        if self.s3 <= x <= self.s4:
            self.minimum = self.s3
            self.maximum = self.s4
            return self.up(x)
        elif x > self.s4:
            return 1
        else:
            return 0
    
    def graph(self, ax, value=None):
        # slow
        # 0 - s1 = 1 [1, 1]
        # s1 - s2 = down [1, 0]
        # s2 - sn = 0 [0, 0]
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        ax.plot(x_slow, y_slow, label='slow')
        # steady
        # 0-s1 = 0 [0, 0]
        # s1 - s2 = up [0, 1]
        # s2 - s3 = 1 [1, 1]
        # s3 - s4 = down [1, 0]
        # s4-sn = 0[0, 0]
        x_steady = [0, self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 0, 1, 1, 0, 0]
        ax.plot(x_steady, y_steady, label='steady')
        # fast
        # 0 - s3 = 0 [0, 0]
        # s3 - s4 =up [0, 1]
        # s4 - sn = 1 [1, 1]
        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        ax.plot(x_fast, y_fast, label='fast')
        ax.set_title('Speed')
        ax.legend(loc='upper right')
        
        if value:
            value_slow = self.slow(value)
            value_steady = self.steady(value)
            value_fast = self.fast(value)
            x_param = [0, value, value]
            # slow
            y_slowvalue = [value_slow, value_slow, 0]
            ax.plot(x_param, y_slowvalue, color='C0')
            # steady
            y_steadyvalue = [value_steady, value_steady, 0]
            ax.plot(x_param, y_steadyvalue, color='C1')
            # fast
            y_fastvalue = [value_fast, value_fast, 0]
            ax.plot(x_param, y_fastvalue, color='C2')

class Pressure(BaseFuzzy):

    def __init__(self):
        self.p1 = 5
        self.p2 = 10
        self.p3 = 15
        self.p4 = 20
        self.p5 = 23
        self.p6 = 27
        self.p7 = 32
        self.p8 = 37
        self.p9 = 40
        self.pn = 60

    def veryLow(self, x) :
      # very low
      # 0-p1 = 1
      # p1-p3 = down
      if x < self.p1:
        return 1
      elif self.p1 <= x <= self.p3:
        self.minimum = self.p1
        self.maximum = self.p3
        return self.down(x)
      else:
        return 0
          
    def low(self, x) :
      # low
      # p2-p3 = up
      # p3-p4 = down
      if self.p2 <= x <= self.p3:
        self.minimum = self.p2
        self.maximum = self.p3
        return self.up(x)
      if self.p3 <= x <= self.p4:
          self.minimum = self.p3
          self.maximum = self.p4
          return self.down(x)
      else:
          return 0
      
    def medium(self, x) :
      # medium
      # p3-p5 = up
      # p5-p6 = 1
      # p6 - p7= down
      if self.p3 <= x <= self.p5:
        self.minimum = self.p3
        self.maximum = self.p5
        return self.up(x)
      if self.p5 <= x <= self.p6:
          return 1
      if self.p6 <= x <= self.p7:
          self.minimum = self.p6
          self.maximum = self.p7
          return self.down(x)
      else:
          return 0
      
    def high(self, x) :
      # high
      # p6 - p7= up
      # p7-p9 = down
      if self.p6 <= x <= self.p7:
        self.minimum = self.p6
        self.maximum = self.p7
        return self.up(x)
      if self.p7 <= x <= self.p9:
          self.minimum = self.p7
          self.maximum = self.p9
          return self.down(x)
      else:
          return 0

    def veryHigh(self, x) :
      # very high
      # p8-p9 = up
      # p9-...=1
      if self.p8 <= x <= self.p9:
        self.minimum = self.p8
        self.maximum = self.p9
        return self.up(x)
      elif x > self.p9:
          return 1
      else:
          return 0
      
    def graph(self, ax, value=None) :
      # very low
      # 0 - p1 = 1 [1, 1]
      # p1 - p3 = down [1, 0]
      # p3 - pn = 0 [0, 0]
      x_veryslow = [0, self.p1, self.p3, self.pn]
      y_veryslow = [1, 1, 0, 0]
      ax.plot(x_veryslow, y_veryslow, label='very low', color='C0')
      # low
      # 0 - p2 = 0 [0, 0]
      # p2 - p3 = up [0, 1]
      # p3 - p4 = down [1, 0]
      # p4 - pn = 0 [0, 0]
      x_slow = [0, self.p2, self.p3, self.p4, self.pn]
      y_slow = [0, 0, 1, 0, 0]
      ax.plot(x_slow, y_slow, label='low', color='C1')
      # medium
      # 0 - p3 = 0 [0, 0]
      # p3 - p5 = up [0, 1]
      # p5 - p6 = 1 [1, 1]
      # p6 - p7 = down [1, 0]
      # p7 - pn = 0 [0, 0]
      x_medium = [0, self.p3, self.p5, self.p6, self.p7, self.pn]
      y_medium = [0, 0, 1, 1, 0, 0]
      ax.plot(x_medium, y_medium, label='medium', color='C2')
      # high
      # 0 - p6 = 0 [0, 0]
      # p6 - p7 = up [0, 1]
      # p7 - p9 = down [1, 0]
      # p9 - pn = 0 [0, 0]
      x_high = [0, self.p6, self.p7, self.p9, self.pn]
      y_high = [0, 0, 1, 0, 0]
      ax.plot(x_high, y_high, label='high', color='C3')
      # very high
      # 0 - p8 = 0 [0, 0]
      # p8 - p9 = up [0, 1]
      # p9 - pn = 1 [1, 1]
      x_veryhigh = [0, self.p8, self.p9, self.pn]
      y_veryhigh = [0, 0, 1, 1]
      ax.plot(x_veryhigh, y_veryhigh, label='very high', color='C4')
      ax.legend(loc='upper right')
      ax.set_title('Pressure')

      if value :
         value_verylow = self.veryLow(value)
         value_low = self.low(value)
         value_medium = self.medium(value)
         value_high = self.high(value)
         value_veryhigh = self.veryHigh(value)
         x_param = [0, value, value]
         # very low
         y_param_veryslow = [value_verylow, value_verylow, 0]
         ax.plot(x_param, y_param_veryslow, color='C0')
         #  low
         y_param_slow = [value_low, value_low, 0]
         ax.plot(x_param, y_param_slow, color='C1')
         # medium
         y_param_medium = [value_medium, value_medium, 0]
         ax.plot(x_param, y_param_medium, color='C2')
         # high
         y_param_high = [value_high, value_high, 0]
         ax.plot(x_param, y_param_high, color='C3')
         # very high
         y_param_veryhigh = [value_veryhigh, value_veryhigh, 0]
         ax.plot(x_param, y_param_veryhigh, color='C4')
        
# Output
class Temperature(BaseFuzzy) :
  minimum = 5
  maximum = 1000
  speed = 0
  pressure = 0

  def __init__(self) :
    self.t1 = 5
    self.t2 = 15
    self.t3 = 25
    self.t4 = 35
    self.tn = 50
    self.speed = 0
    self.pressure = 0
    self.freeze = 0
    self.cold = 0
    self.warm = 0
    self.hot = 0
    self.real_value = 0
      
  def _freeze(self, a) :
    self.freeze = self.t4 - a * (self.t4 - self.t1)
    return self.freeze
  
  def _cold(self, a):
        self.cold = self.t3 - a * (self.t3 - self.t2)
        return self.cold

  def _warm(self, a):
      self.warm = self.t2 - a * (self.t2 - self.t1)
      return self.warm

  def _hot(self, a) :
    self.hot =  a * (self.t4 - self.t1) + self.t1
    return self.hot
  
  # freeze
  # 0 - t1 = 1
  # t1 - t2 = down
  @property
  def fuzzy_freeze(self) :
    x = self.real_value
    if x < self.t1:
      return 1
    elif self.t1 <= x <= self.t2:
      self.minimum = self.t1
      self.maximum = self.t2
      return self.down(x)
    else:
      return 0
  
  # cold
  # t1 - t2 = up
  # t2 - t3 = down
  @property
  def fuzzy_cold(self) :
    x = self.real_value
    if self.t1 <= x <= self.t2:
      self.minimum = self.t1
      self.maximum = self.t2
      return self.up(x)
    if self.t2 <= x <= self.t3:
      self.minimum = self.t2
      self.maximum = self.t3
      return self.down(x)
    else:
      return 0
    
  # warm 
  # t2 - t3 = up
  # t3 - t4 = down
  @property
  def fuzzy_warm(self) :
    x = self.real_value
    if self.t2 <= x <= self.t3:
      self.minimum = self.t2
      self.maximum = self.t3
      return self.up(x)
    if self.t3 <= x <= self.t4:
      self.minimum = self.t3
      self.maximum = self.t4
      return self.down(x)
    else:
      return 0

  # hot
  # t3 - t4 = up
  # t4 - ... = 1
  @property
  def fuzzy_hot(self) :
    x = self.real_value
    if self.t3 <= x <= self.t4:
      self.minimum = self.t3
      self.maximum = self.t4
      return self.up(x)
    elif x > self.t4:
      return 1
    else:
      return 0
    
  def _inferensi(self, spd=Speed(), prs=Pressure()):
    result = []
    # [R1] JIKA Speed SLOW, dan Pressure VERY LOW, MAKA
    # output Temprature HOT.
    a1 = min(spd.slow(self.speed), prs.veryLow(self.pressure))
    z1 = self._hot(a1)
    result.append((a1, z1))
    # [R2] JIKA Speed STEADY, dan Pressure VERY LOW, MAKA
    # output Temprature HOT.
    a2 = min(spd.steady(self.speed), prs.veryLow(self.pressure))
    z2 = self._hot(a2)
    result.append((a2, z2))
    # [R3] JIKA Speed FAST, dan Pressure VERY LOW, MAKA
    # output Temprature HOT.
    a3 = min(spd.fast(self.speed), prs.veryLow(self.pressure))
    z3 = self._hot(a3)
    result.append((a3, z3))
    # [R4] JIKA Speed SLOW, dan Pressure LOW, MAKA
    # output Temprature HOT.
    a4 = min(spd.slow(self.speed), prs.low(self.pressure))
    z4 = self._hot(a4)
    result.append((a4, z4))
    # [R5] JIKA Speed STEADY, dan Pressure LOW, MAKA
    # output Temprature WARM.
    a5 = min(spd.steady(self.speed), prs.low(self.pressure))
    z5 = self._warm(a5)
    result.append((a5, z5))
    # [R6] JIKA Speed FAST, dan Pressure LOW, MAKA
    # output Temprature WARM.
    a6 = min(spd.fast(self.speed), prs.low(self.pressure))
    z6 = self._warm(a6)
    result.append((a6, z6))
    # [R7] JIKA Speed SLOW, dan Pressure MEDIUM, MAKA
    # output Temprature WARM.
    a7 = min(spd.slow(self.speed), prs.medium(self.pressure))
    z7 = self._warm(a7)
    result.append((a7, z7))
    # [R8] JIKA Speed STEADY, dan Pressure MEDIUM, MAKA
    # output Temprature WARM.
    a8 = min(spd.steady(self.speed), prs.medium(self.pressure))
    z8 = self._warm(a8)
    result.append((a8, z8))
    # [R9] JIKA Speed FAST, dan Pressure MEDIUM, MAKA
    # output Temprature COLD.
    a9 = min(spd.fast(self.speed), prs.medium(self.pressure))
    z9 = self._cold(a9)
    result.append((a9, z9))
    # [R10] JIKA Speed SLOW, dan Pressure HIGH, MAKA
    # output Temprature COLD.
    a10 = min(spd.slow(self.speed), prs.high(self.pressure))
    z10 = self._cold(a10)
    result.append((a10, z10))
    # [R11] JIKA Speed STEADY, dan Pressure HIGH, MAKA
    # output Level COLD.
    a11 = min(spd.steady(self.speed), prs.high(self.pressure))
    z11 = self._cold(a11)
    result.append((a11, z11))
    # [R12] JIKA Speed FAST, dan Pressure HIGH, MAKA
    # output Level COLD.
    a12 = min(spd.fast(self.speed), prs.high(self.pressure))
    z12 = self._cold(a12)
    result.append((a12, z12))
    # [R13] JIKA Speed SLOW, dan Pressure VERY HIGH, MAKA
    # output Level FREEZE.
    a13 = min(spd.slow(self.speed), prs.veryHigh(self.pressure))
    z13 = self._freeze(a13)
    result.append((a13, z13))
    # [R14] JIKA Speed STEADY, dan Pressure VERY HIGH, MAKA
    # output Level FREEZE.
    a14 = min(spd.steady(self.speed), prs.veryHigh(self.pressure))
    z14 = self._freeze(a14)
    result.append((a14, z14))
    # [R15] JIKA Speed FAST, dan Pressure VERY HIGH, MAKA
    # output Level FREEZE.
    a15 = min(spd.fast(self.speed), prs.veryHigh(self.pressure))
    z15 = self._freeze(a15)
    result.append((a15, z15))

    return result
  
  def defuzifikasi(self, data_inferensi=[]):
    # ( (α1∗z1) + (α2∗z2) + (α3∗z3) + (α4∗z4) + (α5∗z5) + (α6∗z6) + (α7∗z7) + (α8∗z8) + (α9∗z9) + (α10∗z10) + (α11∗z11) + (α12∗z12) + (α13∗z13) + (α14∗z14) + (α15∗z15) ) / (α1 + α2 + α3 + α4 + α5 + α6 + α7 + α8 + α9 + α10 + α11 + α12 + α13 + α14 + α15)

    data_inferensi = data_inferensi if data_inferensi else self._inferensi()
    res_a_z = 0
    res_a = 0
    for data in data_inferensi:
        # data[0] = a 
        # data[1] = z
        res_a_z += data[0] * data[1]
        res_a += data[0]
    self.real_value = res_a_z / res_a
    return self.real_value
  
  def graph(self) :
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    spd = Speed()
    prs = Pressure()

    spd.graph(ax1, self.speed)
    prs.graph(ax2, self.pressure)
    # freeze
    # 0 - t1 = 1 [1, 1]
    # t1 - t2 = down [1, 0]
    # t2 - tn = 0 [0, 0]
    x_frz = [0, self.t1, self.t2, self.tn]
    y_frz = [1, 1, 0, 0]
    ax3.plot(x_frz, y_frz, label='freeze', color='C0')
    # cold
    # 0 - t1 = 0 [0, 0]
    # t1 - t2 = up [0, 1]
    # t2 - t3 = down [1, 0]
    # t3 - tn = 0 [0, 0]
    x_cld = [0, self.t1, self.t2, self.t3, self.tn]
    y_cld = [0, 0, 1, 0, 0]
    ax3.plot(x_cld, y_cld, label='cold', color='C1')
    # warm
    # 0 - t2 = 0 [0, 0]
    # t2 - t3 = up [0, 1]
    # t3 - t4 = down [1, 0]
    # t4 - tn = 0 [0, 0]
    x_wrm = [0, self.t2, self.t3, self.t4, self.tn]
    y_wrm = [0, 0, 1, 0, 0]
    ax3.plot(x_wrm, y_wrm, label='warm', color='C2')
    # hot
    # 0 - t3 = 0 [0, 0]
    # t3 - t4 = up [0, 1]
    # t4 - tn = 1 [1, 1]
    x_hot = [0, self.t3, self.t4, self.tn]
    y_hot = [0, 0, 1, 1]
    ax3.plot(x_hot, y_hot, label='hot', color='C3')

    ax3.set_title('Temperature [Output]')
    ax3.legend(loc='upper right')

    if self.real_value:
      value = self.real_value
      x_param = [0, value, value]
      # freeze
      frz_value = self.fuzzy_freeze
      y_param_frz = [frz_value, frz_value, 0]
      ax3.plot(x_param, y_param_frz, color='C0')
      # cold
      cld_value = self.fuzzy_cold
      y_param_cld = [cld_value, cld_value, 0]
      ax3.plot(x_param, y_param_cld, color='C1')
      # warm
      wrm_value = self.fuzzy_warm
      y_param_wrm = [wrm_value, wrm_value, 0]
      ax3.plot(x_param, y_param_wrm, color='C2')
      # hot
      hot_value = self.fuzzy_hot
      y_param_hot = [hot_value, hot_value, 0]
      ax3.plot(x_param, y_param_hot, color='C3')

    plt.show()

os.system("cls")
print(f"{'PROGRAM BASEFUZZY':^40}")
print(f"{'-'*40:^40}")
speed = input('Speed : ') 
pressure = input('Pressure : ') 
temperature = Temperature()

# SPEED MAX = 80
# PRESSURE MAX = 40
temperature.speed = float(speed)
temperature.pressure = float(pressure)
hasil_temprature = temperature.defuzifikasi()

print(f'Hasil temprature {hasil_temprature}')
temperature.graph()
    
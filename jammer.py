import random
import time
import math

class Jammer:
    """
    This class simulates jamming by introducing errors, increasing delay, or blocking messages.
    """
    def __init__(self, jamming_probability=0.3, noise_intensity=0.7, jamming_power_dbm=-70):
        self.jamming_probability = jamming_probability
        self.noise_intensity = noise_intensity  # Higher value increases interference
        self.jamming_power_dbm = jamming_power_dbm  # Default jamming signal power in dBm

    def jam_signal(self, message,):
        """Introduce signal degradation or block messages entirely."""
        attack_type = 4
        if random.random() < self.jamming_probability:
            print("[Jammer] Jamming message:", message)
            if random.random() < self.noise_intensity:
                print("[Jammer] Message completely lost!")
                return None, True  # Message is lost
            else:
                if attack_type == 1:
                    self.cw_jamming(message)
                elif attack_type == 2:
                    self.pulsed_noise_jamming(message)
                elif attack_type == 3:
                    self.sweeping_jamming(message)
                elif attack_type == 4:
                    self.directional_jamming(message)
                elif attack_type == 5:
                    return message, False
                else:
                    message['latitude'] += random.uniform(-0.1, 0.1)
                    message['longitude'] += random.uniform(-0.1, 0.1)
                    message['altitude'] += random.uniform(-100, 100)
                return message, True
        return message, False

    def jamming_signal_power(self):
        """Returns the power of the jamming signal in dBm."""
        return self.jamming_power_dbm

    def interfere(self, message, interference):
        message['latitude'] += interference * 0.01  
        message['longitude'] += interference * 0.01
        message['altitude'] += interference
        return message

    def cw_jamming(self, message, frequency=1.0):
        self.noise_intensity = 1
        interference = self.noise_intensity * math.sin(time.time() * frequency ) # Create a sine wave as interferance

        print("CW Jamming")

        return self.interfere(message, interference), True

    
    def sweeping_jamming(self, message, min_freq=0.1, max_freq=5.0 , sweep_rate = 10):
        time_factor = time.time() * sweep_rate
        sweep_freq =  (max_freq - min_freq) * (0.5 * (1 + math.sin(time_factor))) + min_freq # Sweeps sinusoidally

        interference = 0.01 * math.sin(sweep_freq * time_factor)  # Apply sweeping effect

        print("Sweeping Jamming")
        return self.interfere(message, interference), True
    
    def pulsed_noise_jamming(self, message, pulse_rate = 10, pulse_width = 0.2):
        time_factor = time.time() * pulse_rate  # Continious pulsing wave
        pulse_active = (math.sin(time_factor * 2 * math.pi) > (1 - 2 * pulse_width))  # Pulses periodically

        if pulse_active:
            interference = self.noise_intensity * random.uniform(0.5, 1.5)  # Random noise level in pulse
            print("Pulsed Noise Jamming")
            return self.interfere(message, interference), True

    def directional_jamming(self, message):
        # put code here
        return self.interfere(message, 0)
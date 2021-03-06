from model.stats_type import StatsType
import copy


class Stats:
    """This class contains pokemon's statistics and methods to  change them."""

    """Multipliers for statistics changes"""
    multipliers = {
        -6: 0.25,
        -5: 0.29,
        -4: 0.33,
        -3: 0.4,
        -2: 0.5,
        -1: 0.67,
        0: 1,
        1: 1.5,
        2: 2,
        3: 2.5,
        4: 3,
        5: 3.5,
        6: 4
    }

    """Multipliers for accuracy and evasion changes	"""
    multipliersAE = {
        -6: 0.33,
        -5: 0.38,
        -4: 0.43,
        -3: 0.5,
        -2: 0.6,
        -1: 0.75,
        0: 1,
        1: 1.33,
        2: 1.67,
        3: 2,
        4: 2.33,
        5: 2.67,
        6: 3
    }

    def __init__(self, hp: int, attack: int, defense: int, special_attack: int, special_defense: int, speed: int,
                 level=50, is_base=True, ev_speed=252, nature_speed=1.1):
        # Initial value of each statistic
        self.base_stats = {
            StatsType.HP: hp,
            StatsType.Atk: attack,
            StatsType.Def: defense,
            StatsType.Spa: special_attack,
            StatsType.Spd: special_defense,
            StatsType.Spe: speed,
            StatsType.Accuracy: 1,
            StatsType.Evasion: 1
        }

        if is_base:
            self.real_stats = {
                StatsType.HP: round(((31 + (2 * hp) + 0) * level / 100) + 10 + level) + 18,
                StatsType.Atk: round(((31 + (2 * attack) + 0) * level / 100) + 5) + 18,
                StatsType.Def: round(((31 + (2 * defense) + 0) * level / 100) + 5) + 18,
                StatsType.Spa: round(((31 + (2 * special_attack) + 0) * level / 100) + 5) + 18,
                StatsType.Spd: round(((31 + (2 * special_defense) + 0) * level / 100) + 5) + 18,
                StatsType.Spe: round((((31 + (2 * speed) + ev_speed / 4) * level / 100) + 5)) + 18,
                StatsType.Accuracy: 1,
                StatsType.Evasion: 1
            }
        else:
            self.real_stats = self.base_stats

        # Initial value of each statistics' multiplier
        self.mul_stats = {
            StatsType.Atk: 0,
            StatsType.Def: 0,
            StatsType.Spa: 0,
            StatsType.Spd: 0,
            StatsType.Spe: 0,
            StatsType.Accuracy: 0,
            StatsType.Evasion: 0
        }
        # Initial value of each statistics' volatile multiplier
        self.volatile_mul = {
            StatsType.Atk: 1,
            StatsType.Def: 1,
            StatsType.Spa: 1,
            StatsType.Spd: 1,
            StatsType.Spe: 1,
            StatsType.Accuracy: 1,
            StatsType.Evasion: 1
        }
        # Initial value of the damage
        self.damage = 0

    def modify(self, stat_type: StatsType, quantity: int):
        """Changes the multipliers of the specified stat from -6 to 6, these are all set to 0 at the start"""
        if (self.mul_stats[stat_type] + quantity) > 6:
            self.mul_stats[stat_type] = 6
        elif (self.mul_stats[stat_type] + quantity) < -6:
            self.mul_stats[stat_type] = -6
        else:
            self.mul_stats[stat_type] += quantity

    def increase_hp(self, quantity: int):
        """Increase Pokemon's HP by decreasing the damage"""
        if (self.damage - quantity) < 0:
            self.damage = 0
        else:
            self.damage -= round(quantity)

    def decrease_hp(self, quantity: int):
        """Decrease Pokemon's HP by increasing the damage"""
        self.damage = self.real_stats[StatsType.HP] - round(quantity)

    def get_actual(self, stat_type: StatsType) -> int:
        """Returns the requested statistic eventually modified"""
        if stat_type is StatsType.Accuracy or stat_type is StatsType.Evasion:
            return round(self.real_stats[stat_type] * self.multipliersAE[self.mul_stats[stat_type]] * self.volatile_mul[
                stat_type])
        else:
            return round(self.real_stats[stat_type] * self.multipliers[self.mul_stats[stat_type]] * self.volatile_mul[
                stat_type])

    def get_actual_hp(self) -> int:
        """Returns Pokemon's actual HP value by subtracting the damage to the base HP"""
        return self.real_stats[StatsType.HP] - self.damage

    def increase_volatile_mul(self, stats_type: StatsType, value: float):
        """Increases the volatile multiplier of the specified stat by the given value"""
        self.volatile_mul[stats_type] *= value

    def decrease_volatile_mul(self, stats_type: StatsType, value: float):
        """Decreases the volatile multiplier of the specified stat by the given value"""
        self.volatile_mul[stats_type] /= value

    def deepcopy(self):
        new_stats = Stats(0, 0, 0, 0, 0, 0)
        new_stats.base_stats = copy.deepcopy(self.base_stats)
        new_stats.real_stats = copy.deepcopy(self.real_stats)
        new_stats.mul_stats = copy.deepcopy(self.mul_stats)
        new_stats.volatile_mul = copy.deepcopy(self.volatile_mul)
        new_stats.damage = self.damage
        return new_stats

from typing import List


class QtyBag:
    def __init__(self, qty: int, bag):
        self.qty = qty
        self.bag = bag
        self.description = bag.description


class Bag:
    def __init__(self):
        self.description = None
        self.qty_in_parent = 0
        self.contains_bags: List[QtyBag] = []
        self.contained_by = []

    def can_carry_bag(self, bag):
        contained_bag: Bag
        if len(self.contains_bags) == 0:
            return False
        contained_bag: QtyBag
        for contained_bag in self.contains_bags:
            if contained_bag.description == bag.description:
                return True
            elif contained_bag.bag.can_carry_bag(bag):
                return True
        return False

    def count_contained_bags(self):
        contained_bag: QtyBag
        count = 0
        for child_bag in self.contains_bags:
            children_bag_qty = child_bag.bag.count_contained_bags()
            if children_bag_qty:
                count += child_bag.qty * child_bag.bag.count_contained_bags()
            else:
                count += child_bag.qty
        return count + 1


class AllBags:
    def __init__(self, all_bag_rules):
        self._bags = []
        self._all_bag_rules = all_bag_rules
        self.load_bags()
        self.load_bag_contents()

    def bags(self):
        return self._bags

    def load_bags(self):
        for bag_rule in self._all_bag_rules:
            split_bag_rule = bag_rule.split(' contain ')
            bag_description: str = split_bag_rule[0].replace(' bags', '')
            bag = Bag()
            bag.description = bag_description
            self._bags.append(bag)

    def load_bag_contents(self):
        for bag_rule in self._all_bag_rules:
            split_bag_rule = bag_rule.split(' contain ')
            bag_description: str = split_bag_rule[0].replace(' bags', '')
            parent_bag: Bag = self.find_bag(bag_description)
            bag_contents = split_bag_rule[1].split(', ')
            if 'no other bags' in bag_contents[0]:
                continue
            for bag in bag_contents:
                # 1 bright white bag, 2 muted yellow bags.
                s = bag.split()
                inner_bag_description = s[1] + " " + s[2]
                child_bag = self.find_bag(inner_bag_description)
                qty_bag = QtyBag(qty=int(s[0]), bag=child_bag)
                child_bag.contained_by.append(parent_bag)
                parent_bag.contains_bags.append(qty_bag)

    def find_bag(self, description):
        found_bag = None
        for bag in self._bags:
            if description == bag.description:
                found_bag = bag
        return found_bag


def get_parent_bags(all_bag_rules, bag_description):
    all_bags = AllBags(all_bag_rules=all_bag_rules)
    found_bag = all_bags.find_bag(bag_description)
    bags_to_count = []
    for bag in all_bags.bags():
        if bag.can_carry_bag(found_bag):
            bags_to_count.append(bag.description)
    unique_bags = set(bags_to_count)
    return len(unique_bags)


def number_of_contained_bags(all_bag_rules, bag_description):
    all_bags = AllBags(all_bag_rules=all_bag_rules)
    found_bag: Bag = all_bags.find_bag(bag_description)
    bag_count = found_bag.count_contained_bags() - 1  # Subtract self
    return bag_count

from django.contrib.postgres.fields import ArrayField
from django.db import models

# Card - Based on Scryfall Oracle Card JSON Data Model


# TODO: Decide which image URLS must not be blank
class Card(models.Model):
    COMMON = "C"
    UNCOMMON = "UC"
    RARE = "R"
    MYTHIC_RARE = "MR"
    RARITY_CHOICES = [
        (COMMON, "Common"),
        (UNCOMMON, "Uncommon"),
        (RARE, "Rare"),
        (MYTHIC_RARE, "Mythic Rare"),
    ]

    card_subtype = models.CharField("Card subtype", db_index=True, max_length=250)
    card_type = models.CharField(
        "Card's primary type", blank=False, db_index=True, max_length=250
    )
    cmc = models.IntegerField("Card's CMC", db_index=True, default=0)
    color_identity = ArrayField("Card's color identity")
    gatherer_url = models.URLField("Card's Gatherer URL")
    image_small = models.URLField("Card's small image URL")
    image_normal = models.URLField("Card's normal image URL")
    image_large = models.URLField("Card's large image URL")
    image_png = models.URLField("Card's PNG image URL")
    image_art_crop = models.URLField("Card's art crop image URL", max_length=500)
    image_border_crop = models.URLField("Card's border crop image URL")

    mana_cost = ArrayField(models.CharField(), size=8, verbose_name="Card's mana cost")
    name = models.CharField(
        "Card's name", blank=False, db_index=True, max_length=250, unique=True
    )
    oracle_text = models.TextField("The card's text", blank=False)
    rarity = models.CharField(
        "Card's rarity",
        blank=False,
        choices=RARITY_CHOICES,
        db_index=True,
        default=COMMON,
    )
    rulings_url = models.URLField("Card's rulings URL")
    scryfall_url = models.URLField("Scryfall card URL", blank=False)

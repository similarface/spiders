# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class NcbiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Snp_ref(scrapy.Item):
    #RefSNP
    rsid=Field()
    # Organism=Field()
    # MoleculeType=Field()
    # CreatedUpdated=Field()
    # MaptoGenomeBuild=Field()
    # ValidationStatus=Field()
    # Citation=Field()
    # Association=Field()
    # #Allele
    # Variation_Class=Field()
    # RefSNP_Alleles=Field()
    # Allele_Origin=Field()
    Ancestral_Allele=Field()
    # Clinical_Significance=Field()
    # MAF_MinorAlleleCount=Field()
    # #HGVS_Names
    # HGVS_Names=Field()
    RefSNP_Alleles=Field()

    # def __str__(self):
    #     return self.rsid+"-"+self.Ancestral_Allele+"-"+self.RefSNP_Alleles
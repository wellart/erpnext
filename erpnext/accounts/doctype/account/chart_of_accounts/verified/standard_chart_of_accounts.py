# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
from frappe import _

def get():
    return {
        _("Application of Funds (Assets)"): {
          "root_type" : "Asset",
          "account_number" : "1",
          _("Current Assets"): {
            "account_number" : "11",
            "Kas dan Bank" : {
              "account_number" : "111",
              _("Cash In Hand"): {
                "account_type" : "Cash",
                "account_number" : "111-01"
              },
              "Dana Belum Disetor (Rp)" : {
                "account_number" : "111-02"
              },
              _("Bank Accounts"): {
                "account_type" : "Bank",
                "account_number" : "111-11"
              }
            },
            "Piutang Usaha" : {
              "account_number" : "112",
              _("Accounts Receivable"): {
                "account_type" : "Receivable",
                "account_number" : "112-01"
              }
            },
            "Piutang Lain-lain" : {
              "account_number" : "113",
              _("Employee Advances"): {
                "account_number" : "113-01"
              },
              "Piutang Lainnya" : {
                "account_number" : "113-90"
              }
            },
            _("Stock Assets"): {
              "account_number" : "114",
              _("Stock In Hand"): {
                "account_type" : "Stock",
                "account_number" : "114-01"
              },
              "Persediaan Barang Setengah Jadi" : {
                "account_type" : "Stock",
                "account_number" : "114-02"
              },
              "Persediaan Bahan Baku" : {
                "account_type" : "Stock",
                "account_number" : "114-03"
              },
              "Persediaan Lainnya" : {
                "account_type" : "Stock",
                "account_number" : "114-90"
              }
            },
            _("Loans and Advances (Assets)"): {
              "account_number" : "115",
              "Uang Muka Pembelian Barang" : {
                "account_number" : "115-01"
              },
              "Uang Muka Pembelian Aset" : {
                "account_number" : "115-02"
              }
            },
            "Biaya Bayar Dimuka" : {
              "account_number" : "116",
              "Sewa Bayar Dimuka" : {
                "account_number" : "116-01"
              },
              "Asuransi Bayar Dimuka" : {
                "account_number" : "116-02"
              },
              "Perijinan Bayar Dimuka" : {
                "account_number" : "116-03"
              },
              "Biaya Bayar Dimuka Lainnya" : {
                "account_number" : "116-90"
              }
            },
            "Pajak Dibayar Dimuka" : {
              "account_number" : "117",
              "PPN Masukan" : {
                "account_number" : "117-01"
              },
              "Pajak Penghasilan Dibayar Dimuka" : {
                "account_number" : "117-02"
              }
            },
            _("Investments"): {
              "account_number" : "118",
              _("Securities and Deposits"): {
                "account_number" : "118-01"
              }
            },
            "Aset Lancar Lain-lain" : {
              "account_number" : "119",
              _("Temporary Opening"): {
                "account_type" : "Temporary",
                "account_number" : "119-01"
              },
              "Aset Lancar Lainnya" : {
                "account_number" : "119-90"
              }
            }
          },
          _("Fixed Assets"): {
            "account_number" : "12",
            "Tanah" : {
              "account_number" : "121",
              "Tanah" : {
                "account_type" : "Fixed Asset",
                "account_number" : "121-01"
              }
            },
            "Bangunan" : {
              "account_number" : "122",
              _("Buildings"): {
                "account_type" : "Fixed Asset",
                "account_number" : "122-01"
              }
            },
            "Kendaraan" : {
              "account_number" : "123",
              "Kendaraan" : {
                "account_type" : "Fixed Asset",
                "account_number" : "123-01"
              }
            },
            "Peralatan" : {
              "account_number" : "124",
              _("Office Equipments"): {
                "account_type" : "Fixed Asset",
                "account_number" : "124-01"
              },
              _("Plants and Machineries"): {
                "account_type" : "Fixed Asset",
                "account_number" : "124-02"
              },
              _("Electronic Equipments"): {
                "account_type" : "Fixed Asset",
                "account_number" : "124-03"
              },
              _("Furnitures and Fixtures"): {
                "account_type" : "Fixed Asset",
                "account_number" : "124-04"
              }
            },
            "Aset Tak Berwujud" : {
              "account_number" : "125",
              "Lisensi, Paten, Merek Dagang" : {
                "account_type" : "Fixed Asset",
                "account_number" : "125-01"
              },
              "Aset Tak Berwujud Lainnya" : {
                "account_type" : "Fixed Asset",
                "account_number" : "125-90"
              }
            },
            "Akumulasi Penyusutan dan Amortisasi" : {
              "account_number" : "126",
              "Akumulasi Amortisasi Aset Tak Berwujud" : {
                "account_type" : "Accumulated Depreciation",
                "account_number" : "126-31"
              },
              _("Accumulated Depreciation"): {
                "account_type" : "Accumulated Depreciation",
                "account_number" : "126-01"
              },
              "Akumulasi Penyusutan Kendaraan" : {
                "account_type" : "Accumulated Depreciation",
                "account_number" : "126-11"
              },
              "Akumulasi Penyusutan Peralatan" : {
                "account_type" : "Accumulated Depreciation",
                "account_number" : "126-21"
              }
            }
          }
        },
        _("Source of Funds (Liabilities)"): {
          "account_number" : "2",
          "root_type" : "Liability",
          _("Current Liabilities"): {
            "account_number" : "21",
            "Hutang Usaha" : {
              "account_number" : "211",
              _("Accounts Payable"): {
                "account_type" : "Payable",
                "account_number" : "211-01"
              }
            },
            "Uang Muka Konsumen" : {
              "account_number" : "212",
              "Uang Muka Penjualan" : {
                "account_number" : "212-01"
              },
              "Uang Muka Penyewaan" : {
                "account_number" : "212-02"
              }
            },
            _("Stock Liabilities"): {
              "account_number" : "213",
              _("Stock Received But Not Billed"): {
                "account_type" : "Stock Received But Not Billed",
                "account_number" : "213-01"
              }
            },
            "Biaya Yang Masih Harus Dibayar" : {
              "account_number" : "214",
              _("Payroll Payable"): {
                "account_number" : "214-01"
              },
              "Biaya Harus Dibayar - Bonus, THR & Lainnya" : {
                "account_number" : "214-02"
              },
              "Biaya Harus Dibayar - Pengiriman" : {
                "account_number" : "214-03"
              },
              "Biaya Harus Dibayar - Bunga Pinjaman" : {
                "account_number" : "214-04"
              },
              "Biaya Harus Dibayar - Komisi Penjualan" : {
                "account_number" : "214-05"
              },
              "Biaya Harus Dibayar - Lainnya" : {
                "account_number" : "214-90"
              }
            },
            _("Duties and Taxes"): {
              "account_number" : "215",
              "PPN Keluaran" : {
                "account_number" : "215-01"
              },
              "Hutang PPh 21 - Karyawan" : {
                "account_number" : "215-02"
              },
              "Hutang PPh 23 - Badan" : {
                "account_number" : "215-03"
              },
              "Hutang Pajak Lainnya" : {
                "account_number" : "215-90"
              }
            }
          },
          "Pinjaman" : {
            "account_number" : "22",
            _("Loans (Liabilities)"): {
              "account_number" : "221",
              _("Secured Loans"): {
                "account_number" : "221-01"
              },
              _("Unsecured Loans"): {
                "account_number" : "221-02"
              }
            },
            "Hutang Pembelian Aset": {
              "account_number" : "222",
              "Hutang Cicilan Kendaraan" : {
                "account_number" : "222-01"
              },
              "Hutang Cicilan Properti" : {
                "account_number" : "222-02"
              }
            },
            "Hutang Bunga Pinjaman" : {
              "account_number" : "223",
              "Hutang Bunga Pinjaman Bank" : {
                "account_number" : "223-01"
              },
              "Hutang Bunga Pinjaman Pada Pihak Lain" : {
                "account_number" : "223-02"
              },
              "Hutang Bunga Pembelian Secara Kredit" : {
                "account_number" : "223-03"
              }
            }
          }
        },
        _("Equity"): {
          "account_number" : "3",
          "root_type" : "Equity",
          "Modal" : {
            "account_number" : "31",
            "Permodalan" : {
              "account_number" : "311",
              _("Opening Balance Equity"): {
                "account_type" : "Equity",
                "account_number" : "311-01"
              },
              _("Capital Stock"): {
                "account_type" : "Equity",
                "account_number" : "311-02"
              },
              "Modal Bantuan/Hibah" : {
                "account_type" : "Equity",
                "account_number" : "311-03"
              },
              "Pengambilan Modal Oleh Pemilik" : {
                "account_type" : "Equity",
                "account_number" : "311-11"
              }
            }
          },
          "Laba" : {
            "account_number" : "32",
            "Laba" : {
              "account_number" : "321",
              "Laba Tahun Berjalan" : {
                "account_type" : "Equity",
                "account_number" : "321-01"
              },
              _("Retained Earnings"): {
                "account_type" : "Equity",
                "account_number" : "321-02"
              }
            }
          }
        },
        _("Income"): {
          "account_number" : "4",
          "root_type" : "Income",
          _("Direct Income"): {
            "account_number" : "41",
            "Penjualan" : {
              "account_number" : "411",
              _("Sales"): {
                "account_type" : "Income Account",
                "account_number" : "411-01"
              },
              _("Service"): {
                "account_number" : "411-11"
              },
              "Pendapatan Sewa" : {
                "account_number" : "411-21"
              }
            }
          },
          _("Indirect Income"): {
            "account_number" : "42",
            "Pendapatan Lain-lain" : {
              "account_number" : "421",
              "Pendapatan Komisi" : {
                "account_number" : "421-01"
              },
              "Pendapatan Ongkos Penjualan" : {
                "account_number" : "421-02"
              },
              "Pendapatan Bunga Bank" : {
                "account_number" : "421-03"
              },
              "Pendapatan Bunga Dari Pihak Lain" : {
                "account_number" : "421-04"
              },
              "Pendapatan Lainnya" : {
                "account_number" : "421-90"
              }
            }
          }
        },
        _("Expenses"): {
          "account_number" : "5",
          "root_type" : "Expense",
          _("Direct Expenses"): {
            "account_number" : "51",
            _("Stock Expenses"): {
              "account_number" : "511",
              _("Cost of Goods Sold"): {
                "account_type" : "Cost of Goods Sold",
                "account_number" : "511-01"
              },
              _("Expenses Included In Valuation"): {
                "account_type" : "Expenses Included In Valuation",
                "account_number" : "511-02"
              },
              "Biaya Kemasan" : {
                "account_number" : "511-03"
              },
              _("Freight and Forwarding Charges"): {
                "account_type" : "Chargeable",
                "account_number" : "511-04"
              },
              "Beban Barang Susut & Rusak" : {
                "account_type" : "Expense Account",
                "account_number" : "511-05"
              },
              _("Stock Adjustment"): {
                "account_type" : "Stock Adjustment",
                "account_number" : "511-06"
              }
            },
            "Biaya Pemasaran" : {
              "account_number" : "512",
              _("Marketing Expenses"): {
                "account_type" : "Chargeable",
                "account_number" : "512-01"
              },
              "Beban Bonus, Hadiah & Sampel" : {
                "account_number" : "512-02"
              },
              _("Commission on Sales"): {
                "account_number" : "512-03"
              },
              "Biaya Pameran" : {
                "account_number" : "512-04"
              },
              "Biaya Pemasaran Lainnya" : {
                "account_number" : "512-90"
              }
            }
          },
          "Biaya Operasional" : {
            "account_number" : "52",
            "Biaya Personal" : {
              "account_number" : "521",
              _("Salary"): {
                "account_number" : "521-01"
              },
              "Biaya Lembur, THR & Bonus" : {
                "account_number" : "521-02"
              },
              "Biaya Pengobatan" : {
                "account_number" : "521-03"
              },
              "Biaya Pendidikan & Pelatihan" : {
                "account_number" : "521-04"
              },
              "PPh 21" : {
                "account_number" : "521-05"
              },
              "BPJS Kesehatan" : {
                "account_number" : "521-06"
              },
              "BPJS Tenaga Kerja" : {
                "account_number" : "521-07"
              },
              "Biaya Asuransi Lainnya" : {
                "account_number" : "521-08"
              },
              "Biaya Personal Lainnya" : {
                "account_number" : "521-90"
              }
            },
            "Biaya Administrasi & Umum" : {
              "account_number" : "522",
              _("Print and Stationery"): {
                "account_type" : "Expense Account",
                "account_number" : "522-01"
              },
              _("Telephone Expenses"): {
                "account_type" : "Expense Account",
                "account_number" : "522-02"
              },
              _("Utility Expenses"): {
                "account_type" : "Expense Account",
                "account_number" : "522-03"
              },
              _("Postal Expenses"): {
                "account_type" : "Expense Account",
                "account_number" : "522-04"
              },
              _("Entertainment Expenses"): {
                "account_type" : "Expense Account",
                "account_number" : "522-05"
              },
              _("Travel Expenses"): {
                "account_type" : "Expense Account",
                "account_number" : "522-06"
              },
              "Biaya Iuran dan Langganan" : {
                "account_type" : "Expense Account",
                "account_number" : "522-07"
              },
              "Biaya Konsumsi" : {
                "account_type" : "Expense Account",
                "account_number" : "522-08"
              },
              _("Office Rent"): {
                "account_type" : "Expense Account",
                "account_number" : "522-09"
              },
              "Biaya Peralatan" : {
                "account_type" : "Expense Account",
                "account_number" : "522-10"
              },
              _("Office Maintenance Expenses"): {
                "account_type" : "Expense Account",
                "account_number" : "522-11"
              },
              "Biaya Asuransi Non-Pegawai" : {
                "account_type" : "Expense Account",
                "account_number" : "522-12"
              },
              _("Legal Expenses"): {
                "account_type" : "Expense Account",
                "account_number" : "522-13"
              }
            },
            "Biaya Operasional Lain-lain" : {
              "account_number" : "523",
              _("Miscellaneous Expenses"): {
                "account_type" : "Expense Account",
                "account_number" : "523-90"
              }
            }
          },
          "Biaya Non Operasional" : {
            "account_number" : "53",
            "Biaya Non Operasional" : {
              "account_number" : "531",
              _("Administrative Expenses"): {
                "account_type" : "Chargeable",
                "account_number" : "531-01"
              },
              "Biaya Provisi Pinjaman bank" : {
                "account_type" : "Chargeable",
                "account_number" : "531-02"
              },
              _("Round Off"): {
                "account_type" : "Round Off",
                "account_number" : "531-03"
              },
              _("Exchange Gain/Loss"): {
                "account_number" : "531-04"
              },
              "Beban Bunga Pinjaman" : {
                "account_number" : "531-05"
              },
              _("Gain/Loss on Asset Disposal"): {
                "account_number" : "531-06"
              },
              "Kerugian Bencana" : {
                "account_number" : "531-07"
              },
              _("Write-Off"): {
                "account_number" : "531-08"
              },
              "Beban Piutang Tak Tertagih" : {
                "account_type" : "Expense Account",
                "account_number" : "531-09"
              }
            },
            "Beban Pajak" : {
              "account_number" : "532",
              "Beban Pajak Bumi & Bangunan" : {
                "account_type" : "Tax",
                "account_number" : "532-01"
              },
              "Beban Pajak Penghasilan" : {
                "account_type" : "Tax",
                "account_number" : "532-02"
              },
              "Beban Pajak PPN" : {
                "account_type" : "Tax",
                "account_number" : "532-03"
              },
              "Beban Pajak Rekening Bank" : {
                "account_type" : "Tax",
                "account_number" : "532-04"
              },
              "Beban Pajak Lainnya" : {
                "account_type" : "Tax",
                "account_number" : "532-90"
              }
            },
            "Beban Penyusutan & Amortisasi" : {
              "account_number" : "533",
              "Beban Amortisasi Aset Tak Berwujud" : {
                "account_type" : "Depreciation",
                "account_number" : "533-31"
              },
              _("Depreciation"): {
                "account_type" : "Depreciation",
                "account_number" : "533-01"
              },
              "Beban Penyusutan Kendaraan" : {
                "account_type" : "Depreciation",
                "account_number" : "533-11"
              },
              "Beban Penyusutan Peralatan" : {
                "account_type" : "Depreciation",
                "account_number" : "533-21"
              }
            }
          }
        }
      }
